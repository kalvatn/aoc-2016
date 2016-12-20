from stdlib import aoc

class Day20(aoc.Day):
    def __init__(self):
        super(Day20, self).__init__(__file__)

    def run(self):
        max_allowed = 4294967295
        lines = sorted(self.read_input(), key=lambda l: int(l.split('-')[0]))
        ranges = []

        for line in lines:
            start, end = [ int(i) for i in line.split('-') ]
            ranges.append((start, end))

        smallest = 0
        for start, end in ranges:
            if smallest >= start and start <= end:
                smallest = end + 1

        self.log.debug('part 1 : %s' % (smallest))


if __name__ == '__main__':
    Day20().run()
