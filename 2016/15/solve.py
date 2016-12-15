#!/usr/bin/env python

import unittest
import re


class Disc(object):
    def __init__(self, number, positions, current):
        self.number = number
        self.positions = positions
        self.current = current

    def __str__(self):
        return '%d - %d/%d' % (self.number, self.current, self.positions)

    def __repr__(self):
        return str(self)

def main(lines):

    discs = []
    pattern = re.compile(r'Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)')
    for line in lines:
        match = pattern.match(line)
        number, positions, start = [ int (g) for g in match.groups() ]
        discs.append(Disc(number, positions, start))

    print discs


    part1 = None
    part2 = None


    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    # with open('input') as file:
    with open('example_input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
