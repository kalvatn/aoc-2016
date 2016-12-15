#!/usr/bin/env python

import unittest
import time
import os

ON  = '#'
OFF = '.'

class Light(object):
    def __init__(self, x, y, state, always_on=False):
        self.x = x
        self.y = y

        self.always_on = always_on
        self.state = ON if always_on else state
        self.neighbours = []
        self.next_state = None

    def prepare_next_state(self):
        if self.always_on:
            self.next_state = ON
            return

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

def create_grid(lines, static_lights=[]):
    length = len(lines[0])
    grid = [ [ Light(x, y, lines[y][x], always_on = (y,x) in static_lights) for x in range(0, length) ] for y in range(0, length) ]
    for y in range(0, length):
        for x in range(0, length):
            light = grid[y][x]
            neighbours = []
            for nx, ny in [ (x + dx, y + dy) for dx, dy in [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ] if (x + dx >= 0 and x + dx < length) and (y + dy >= 0 and y + dy < length) ]:
                neighbours.append(grid[ny][nx])
            light.neighbours = neighbours
    return grid

def run_simulation(grid, max_steps, visualize=False, visualize_sleep=0.05):
    for i in range(0, max_steps):
        if visualize:
            os.system('clear')
            print 'step %d' % i
            print_grid(grid)
            time.sleep(visualize_sleep)

        for light in [ light for row in grid for light in row]:
            light.prepare_next_state()

        for light in [ light for row in grid for light in row]:
            light.apply_next_state()

def get_input_lines(input_file='input'):
    return [ line.strip() for line in open(input_file) ]

def get_lights_on(grid):
    return len([light for light in [ light for row in grid for light in row] if light.state == ON])

def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()

    grid = create_grid(example_lines)
    run_simulation(grid, 5, visualize=False)
    part1_example = get_lights_on(grid)

    grid = create_grid(lines)
    run_simulation(grid, 100)
    part1 = get_lights_on(grid)

    grid = create_grid(example_lines, static_lights=[(0,0), (0,5), (5,0), (5, 5)])
    run_simulation(grid, 5, visualize=True)
    part2_example = get_lights_on(grid)

    grid = create_grid(get_input_lines(), static_lights=[(0,0), (0,99), (99,0), (99, 99)])
    run_simulation(grid, 100, visualize=True)
    part2 = get_lights_on(grid)


    print 'part 1 example : %s' % (part1_example)
    print 'part 2 example : %s' % (part2_example)
    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    main()
else:
    main()
