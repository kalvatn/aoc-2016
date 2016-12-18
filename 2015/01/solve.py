#!/usr/bin/env python

from stdlib import aoc

LEFT_PAREN  = '('
RIGHT_PAREN = ')'

class Day1(aoc.Day):
    def __init__(self):
        super(Day1, self).__init__(__file__)

    def run(self):
        lines = self.read_input()
        parens = lines[0]
        floor = 0
        position = 0
        basement_found = False
        for paren in parens:
            updown = 1 if paren == LEFT_PAREN else -1

            floor += updown
            if not basement_found:
                position += 1
                if floor == -1:
                    basement_found = True

        self.log.info('part 1 : %d' % (floor))
        self.log.info('part 2 : %d' % (position))

if __name__ == '__main__':
    Day1().run()

