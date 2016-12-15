#!/usr/bin/env python

import unittest
import time
import os

ON  = '#'
OFF = '.'

class Light(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y

        self.state = state
        self.neighbours = []
        self.next_state = None

    def prepare_next_state(self):
        neighbours_on = len([ n for n in self.neighbours if n.state == ON])
        if self.state == ON:
            self.next_state = ON if neighbours_on in [2, 3] else OFF
        else:
            self.next_state = ON if neighbours_on == 3 else OFF

    def apply_next_state(self):
        self.state = self.next_state

    def __str__(self):
        return '%s (%d, %d)' % (self.state, self.x, self.y)

    def __repr__(self):
        return str(self)


def print_grid(grid):
    out = ''
    for row in grid:
        r = ''
        for col in row:
            r += col.state
        out += r + '\n'

    print out

def main(lines):
    length = len(lines[0])
    grid = [ [ Light(x, y, lines[y][x]) for x in range(0, length) ] for y in range(0, length) ]
    for y in range(0, length):
        for x in range(0, length):
            light = grid[y][x]
            neighbours = []
            for nx, ny in [ (x + dx, y + dy) for dx, dy in [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ] if (x + dx >= 0 and x + dx < length) and (y + dy >= 0 and y + dy < length) ]:
                neighbours.append(grid[ny][nx])
            light.neighbours = neighbours



    max_steps = 5
    sleep = 0.05
    for i in range(0, max_steps):
        os.system('clear')
        print 'step %d' % i
        print_grid(grid)
        for light in [ light for row in grid for light in row]:
            light.prepare_next_state()

        for light in [ light for row in grid for light in row]:
            light.apply_next_state()
        time.sleep(sleep)

    part1 = len([light for light in [ light for row in grid for light in row] if light.state == ON])
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
