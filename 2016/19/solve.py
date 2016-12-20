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

    def run(self):
        line = self.read_input()[0]

        # number_of_elves = int(line)
        number_of_elves = 5

        elves = self.generate_elves(number_of_elves)
        elf = elves[0]
        while elf.next != elf:
            next_elf = elf.next
            self.log.debug("elf %d takes elf %d's %d presents" % (elf.number, next_elf.number, next_elf.presents))
            elf.take_presents_from_next()
            elf = elf.next
        self.log.debug('%d elves : winner : %s' % (number_of_elves, elf))

    def generate_elves(self, number_of_elves):
        elves = []
        for i in range(1, number_of_elves + 1):
            elves.append(Elf(i))
        head = elves[0]
        tail = elves[-1]
        for i in range(0, len(elves)):
            elf = elves[i]
            if i + 1 >= len(elves):
                elf.next = head
            else:
                elf.next = elves[i+1]
            if i - 1 < 0:
                elf.prev = tail
            else:
                elf.prev = elves[i-1]

        return elves

if __name__ == '__main__':
    Day19().run()
