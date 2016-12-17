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
    UP = (-1, 0, 'U')
    DOWN = (1, 0, 'D')
    RIGHT = (0, 1, 'R')
    LEFT = (0, -1, 'L')

def get_hash_start(passcode):
    return hashlib.md5(passcode).hexdigest()[0:4]

def get_directions_from_hash(hashed):
    directions = set()

    if hashed[0] in 'bcdef':
        directions.add(Direction.UP)
    if hashed[1] in 'bcdef':
        directions.add(Direction.DOWN)
    if hashed[2] in 'bcdef':
        directions.add(Direction.LEFT)
    if hashed[3] in 'bcdef':
        directions.add(Direction.RIGHT)

    return directions

def get_moves(current, grid):
    moves = set()
    y, x, passcode = current
    hashed = get_hash_start(passcode)
    for dy, dx, d in get_directions_from_hash(hashed):
        nx = x + dx
        ny = y + dy

        try:
            if grid[ny][nx] == WALL:
                continue

            if grid[ny][nx] in '|-':
                if d == 'D':
                    ny += 1
                elif d == 'U':
                    ny -= 1
                elif d == 'L':
                    nx -= 1
                elif d == 'R':
                    nx += 1

            # debug('(%d, %d): %s' % (ny, nx, grid[ny][nx]))
            moves.add((ny, nx, passcode + d))
        except IndexError:
            warn('oob? (%d, %d)' % (ny, nx))
    return moves



def get_grid(map_lines):
    grid = [ [ map_lines[y][x] for x in range(0, len(map_lines[y])) ] for y in range(0, len(map_lines)) ]
    # due to vim stripping newlines O_o
    grid[7].append(' ')
    grid[7].append(' ')
    return grid

def print_grid(grid):
    out = ''
    for y in range(0, len(grid)):
        out += ''
        for x in range(0, len(grid)):
            out += grid[y][x]
        out += '\n'
    print out


def bfs(start, goal, grid, find_longest=False):
    visited = set()
    fringe = set([start])
    steps = 0
    paths = []
    while len(fringe) > 0:
        new_fringe = set()
        for current in fringe:
            y, x, passcode = current
            if (y, x) == goal:
                if not find_longest:
                    debug('found in %d steps' % steps)
                    return passcode.replace(start[2], '')
                else:
                    paths.append(passcode.replace(start[2], ''))
            else:
                hashed = get_hash_start(passcode)
                directions = get_directions_from_hash(hashed)

                visited.add(current)
                for move in get_moves(current, grid):
                    if move not in visited:
                        # debug('candidate move : %s' % str(move))
                        new_fringe.add(move)
        fringe = new_fringe
        steps += 1


    if find_longest and not paths:
        raise ValueError('not found')

    return max(map(len, paths))




def main():
    map_lines = get_input_lines(input_file='map_input')
    grid = get_grid(map_lines)
    print 'part 1 : %s' % bfs( (1, 1, 'pslxynzg'), (7, 7), grid)
    print 'part 2 : %d' % bfs( (1, 1, 'pslxynzg'), (7, 7), grid, True)


class Test(unittest.TestCase):
    def setUp(self):
        self.grid = get_grid(get_input_lines(input_file='map_input'))
    # @unittest.skip('skip')
    def test_get_hash_start(self):
        self.assertEquals(get_hash_start('hijkl'), 'ced9')
    def test_get_directions_from_hash(self):
        self.assertEquals(get_directions_from_hash('ced9'), set([Direction.UP, Direction.DOWN, Direction.LEFT]))
        self.assertEquals(get_directions_from_hash('f2bc'), set([Direction.UP, Direction.LEFT, Direction.RIGHT]))

    def test_get_moves(self):
        moves = get_moves((1,1, 'hijkl'), self.grid)
        self.assertEquals(moves, set( [ (3, 1, 'hijklD') ]))

        moves = get_moves((2,1, 'hijklD'), self.grid)
        self.assertEquals(moves, set( [ (1, 1, 'hijklDU') ]))

    def test_find_shortest_path(self):
        print_grid(self.grid)
        goal = (7,7)
        self.assertEquals(bfs((1, 1, 'ihgpwlah'), goal, self.grid), 'DDRRRD')
        self.assertEquals(bfs((1, 1, 'kglvqrro'), goal, self.grid), 'DDUDRLRRUDRD')
        self.assertEquals(bfs((1, 1, 'ulqzkmiv'), goal, self.grid), 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

    def test_find_longest_path_length(self):
        print_grid(self.grid)
        goal = (7,7)
        self.assertEquals(bfs((1, 1, 'ihgpwlah'), goal, self.grid, True), 370)
        self.assertEquals(bfs((1, 1, 'kglvqrro'), goal, self.grid, True), 492)
        self.assertEquals(bfs((1, 1, 'ulqzkmiv'), goal, self.grid, True), 830)


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
            print _CSI + _COLORS[color] + str(message) + _RESET
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
