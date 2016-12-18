#!/usr/bin/env python
from stdlib import aoc

class Day10(aoc.Day):
    def __init__(self):
        return super(Day10, self).__init__(__file__)

    def run(self):
        for sequence in self.read_input():
            original = sequence
            for i in range(0, 40):
                sequence = self.new_sequence(sequence)

            self.log.info('part 1 : %s' % (len(sequence)))
            sequence = original
            for i in range(0, 50):
                sequence = self.new_sequence(sequence)

            self.log.info('part 2 : %s' % (len(sequence)))

    def new_sequence(self, sequence):
        digit = sequence[0]
        count = 0
        builder = []
        for i in sequence:
            if i != digit:
                builder.append(str(count) + digit)
                digit = i
                count = 0
            count += 1

        builder.append(str(count) + digit)
        return ''.join(builder)

if __name__ == '__main__':
    Day10().run()
