import time
from stdlib import aoc

class Elf(object):
    def __init__(self, number):
        self.number = number
        self.has_presents = True


class Day19(aoc.Day):
    def __init__(self):
        super(Day19, self).__init__(__file__)

    def run(self):
        line = self.read_input()[0]
        elves = {}

        # for i in range(0, 10):
        number_of_elves = int(line)
        # number_of_elves = 5
        for i in range(1, number_of_elves+1):
            if i not in elves:
                elves[i] = 1
        part1, part2 = None, None
        part1 = self.part_one(elves, number_of_elves)
        self.log.info('part 1 : %s' % (part1))

        part2 = self.part_two(elves, number_of_elves)
        self.log.info('part 2 : %s' % (part2))

    def next_in_circle(self, prev, elves):
        next_in_circle = prev + 1
        if next_in_circle > len(elves):
            next_in_circle = 1

        while elves[next_in_circle] == 0:
            next_in_circle += 1
            if next_in_circle > len(elves):
                next_in_circle = 1
        return next_in_circle

    def part_one(self, elves, number_of_elves):
        stealer = 0
        elves_with_presents = len(elves)
        while elves_with_presents > 1:
            stealer = self.next_in_circle(stealer, elves)
            stealee = self.next_in_circle(stealer, elves)
            # self.log.debug("elf %d takes elf %d's %d presents" % (stealer, stealee, elves[stealee]))
            elves[stealer] = elves[stealer] + elves[stealee]
            elves[stealee] = 0
            elves_with_presents -= 1
        return [ k for k, v in elves.items() if v >= 1 ][0]

    def part_two(self, elves, number_of_elves):
        i = 0
        elves_with_presents = len(elves)
        while elves_with_presents > 1:
            i = 0 if i % number_of_elves == 0 else i
            while elves[i] == 0:
                self.log.debug('elf %d has no presents and is skipped' % (i + 1))
                i += 1
                i = 0 if i % number_of_elves == 0 else i


            mid = i + elves_with_presents / 2
            print 'i : %d, mid : %d, elves_with_presents : %d' % (i, mid, elves_with_presents)

            steal_from = mid - 1
            # steal_from = i + 1 if i + 1 < number_of_elves else 0
            while elves[steal_from] == 0:
                self.log.debug('elf %d has no presents and is skipped' % (steal_from + 1))
                steal_from = steal_from + 1 if steal_from + 1 < number_of_elves else 0

                if self.visualize:
                    time.sleep(1)

            self.log.debug("elf %d takes elf %d's %d presents" % (i+1, steal_from+1, elves[steal_from]))
            elves[i] = elves[i] + elves[steal_from]
            elves[steal_from] = 0
            elves_with_presents -= 1
            i += 1

            if self.visualize:
                time.sleep(1)

        return [ k+1 for k, v in elves.items() if v >= 1 ][0]








if __name__ == '__main__':
    Day19().run()
