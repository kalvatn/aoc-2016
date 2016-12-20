from stdlib import aoc

class Day20(aoc.Day):
    def __init__(self):
        super(Day20, self).__init__(__file__)

    def run(self):
        lines = sorted(self.read_input(), key=lambda l: int(l.split('-')[0]))
        ranges = []
        for line in lines:
            start, end = [ int(i) for i in line.split('-') ]
            ranges.append((start, end))

        self.log.info('part 1 : %s' % (self.get_smallest_allowed(ranges)))
        self.log.info('part 2 : %s' % (len(self.get_allowed_ips(ranges))))

    def get_smallest_allowed(self, ranges):
        smallest = 0
        for start, end in ranges:
            if smallest >= start and start <= end:
                smallest = end + 1
        return smallest

    def get_allowed_ips(self, ranges, highest=4294967295):
        i = 0
        ips = set()
        while i <= highest:
            for start, end in ranges:
                if start <= i <= end:
                    i = end + 1
                    continue
            else:
                if i <= highest:
                    ips.add(i)
                i += 1
        return ips




if __name__ == '__main__':
    Day20().run()
