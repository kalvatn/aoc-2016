import time
from stdlib import aoc

class Elf(object):
    def __init__(self, number):
        self.number = number
        self.presents = 1
        self.prev = None
        self.next = None

    def take_presents_from_next(self):
        self.presents += self.next.presents
        self.next.presents = 0
        self.next.leave_ring()

    def take_presents_from_across(self, across):
        self.presents += across.presents
        across.presents = 0
        across.leave_ring()

    def leave_ring(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def __str__(self):
        return 'elf %d : %d presents' % (self.number, self.presents)

    def __repr__(self):
        return '%d' % (self.number)

class Day19(aoc.Day):
    def __init__(self):
        super(Day19, self).__init__(__file__)


    def generate_elves(self, number_of_elves, across=False):
        elves = []
        for i in range(0, number_of_elves):
            elf = Elf(i+1)
            if i > 0:
                elf.prev = elves[i-1]
                elves[i-1].next = elf
            elves.append(elf)
        head = elves[0]
        tail = elves[-1]
        head.prev = tail
        tail.next = head

        return elves

    def part_one(self, number_of_elves):

        elves = self.generate_elves(number_of_elves)
        elf = elves[0]
        while elf.next != elf:
            next_elf = elf.next
            # self.log.debug("elf %d takes elf %d's %d presents" % (elf.number, next_elf.number, next_elf.presents))
            elf.take_presents_from_next()
            elf = elf.next
        return elf

    def part_two(self, number_of_elves):

        elves = self.generate_elves(number_of_elves)

        elf = elves[0]
        across = elves[number_of_elves / 2]
        while number_of_elves > 1:
            # self.log.debug("elf %d takes elf %d's %d presents" % (elf.number, across.number, across.presents))
            elf.take_presents_from_across(across)
            elf = elf.next
            across = across.next
            if number_of_elves % 2 == 1:
                across = across.next
            number_of_elves -= 1
        return elf

    def run(self):
        line = self.read_input()[0]

        number_of_elves = int(line)
        # number_of_elves = 21

        self.log.info('part1 : %s' % (self.part_one(number_of_elves)))
        self.log.info('part2 : %s' % (self.part_two(number_of_elves)))


if __name__ == '__main__':
    Day19().run()
