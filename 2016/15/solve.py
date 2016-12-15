#!/usr/bin/env python

import unittest
import re

import time


class Disc(object):
    def __init__(self, number, positions, current):
        self.number = number
        self.positions = positions
        self.current = current

    def tick(self):
        self.current += 1
        if self.current % self.positions == 0:
            self.current = 0

    def __str__(self):
        # return '%d - %d' % (self.number, self.current)
        return '%d' % (self.current)

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
    i = 0
    while True:
        if all(discs[t].current + t == discs[t].positions - 1 for t in range(0, len(discs))):

            print '%2d : %s' % (i, discs)
            part1 = i
            break

        for disc in discs:
            disc.tick()
        i += 1

    part2 = None


    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
    # with open('example_input') as file:
    # with open('custom_input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
