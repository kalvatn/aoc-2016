#!/usr/bin/env python

import unittest
import sys
import os
import time
import hashlib
# from itertools import permutations
# from itertools import combinations_with_replacement
# from itertools import combinations
# import deque

VERBOSE = False
RUN_TESTS = False
VISUALIZE = False

WALL, DOOR_LR, DOOR_UD = '#', '|', '-'

class Direction(object):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

def get_hash_start(passcode):
    return hashlib.md5(passcode).hexdigest()[0:4]

def get_directions_from_hash(hashed):
    directions = set()
    up, down, left, right = hashed
    for d in [ up, down, left, right ]:
        if d in 'bcdef':
            if d == up:
                directions.add(Direction.UP)
            elif d == down:
                directions.add(Direction.DOWN)
            elif d == left:
                directions.add(Direction.LEFT)
            elif d == right:
                directions.add(Direction.RIGHT)
    return directions



def get_grid(map_lines):
    return [ [ map_lines[y][x] for x in range(0, len(map_lines[y])) ] for y in range(0, len(map_lines)) ]

def print_grid(grid):
    out = ''
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            out += grid[y][x]
        out += '\n'
    print out


def main():
    map_lines = get_input_lines(input_file='map_input')
    grid = get_grid(map_lines)
    print_grid(grid)

    start = (0, 0)


class Test(unittest.TestCase):
    # @unittest.skip('skip')
    def test_get_hash_start(self):
        self.assertEquals(get_hash_start('hijkl'), 'ced9')
    def test_get_directions_from_hash(self):
        self.assertEquals(get_directions_from_hash('ced9'), set([Direction.UP, Direction.DOWN, Direction.LEFT]))
        self.assertEquals(get_directions_from_hash('f2bc'), set([Direction.UP, Direction.LEFT, Direction.RIGHT]))

def get_input_lines(input_file='input'):
    try:
        return [ line.strip() for line in open(input_file) ]
    except:
        warn('could not read input file %s' % input_file)
        return []

def debug(message):
    if VERBOSE:
        _print(message, color='green')

def warn(message):
    _print(message, color='yellow')

def info(message):
    print message

def error(message):
    _print(message, color='red')
    sys.exit(1)

def _print(message, color='default'):
    if color == 'default':
        print message
    else:
        _COLORS = {
            'red' : '31m',
            'green' : '32m',
            'yellow' : '33m',
            'blue' : '34m',
            'magenta' : '35m',
            'cyan' : '36m'
        }
        _CSI = "\x1B["
        _RESET=_CSI+"0m"
        if color in _COLORS:
            print _CSI + _COLORS[color] + message + _RESET
        else:
            print message



def process_args(args):
    global RUN_TESTS
    global VISUALIZE
    global VERBOSE
    if args:
        VISUALIZE = '--visualize' in args
        VERBOSE = '--verbose' in args or '-v' in args
        RUN_TESTS = '--test' in args or '-t' in args
    if RUN_TESTS:
        args = []
        unittest.main(argv=[sys.argv[0]])
    debug('VERBOSE=%s, VISUALIZE=%s (%s)' % (VERBOSE, VISUALIZE, args))

if __name__ == '__main__':
    process_args(sys.argv[1:])
    main()
else:
    process_args(sys.argv[1:])
    main()
