#!/usr/bin/env python

import unittest
import sys
import os
import time
# from itertools import permutations
# from itertools import combinations_with_replacement
# from itertools import combinations
# import deque

VERBOSE = False
RUN_TESTS = False
VISUALIZE = False

TRAP = '^'
SAFE = '.'

RULE_1 = (TRAP * 2) + SAFE
RULE_2 = SAFE + (TRAP * 2)
RULE_3 = TRAP + (2 * SAFE)
RULE_4 = (SAFE * 2) + TRAP
TRAP_RULES = [ RULE_1, RULE_2, RULE_3, RULE_4 ]

def generate(line):
    next_line = ''
    for i in range(0, len(line)):
        l = line[i-1] if i > 0 else SAFE
        r = line[i+1] if i < len(line) - 1 else SAFE
        c = line[i]

        if l + c + r in TRAP_RULES:
            next_line += TRAP
        else:
            next_line += SAFE
    return next_line


def solve(line, rows):
    count_safe = line.count(SAFE)
    debug('%s (%d)' % (line, count_safe))
    for i in range(0, rows - 1):
        new_line = generate(line)
        line_safe = new_line.count(SAFE)
        count_safe += line_safe
        debug('%s (%d)' % (new_line, line_safe))
        line = new_line
    return count_safe


def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()

    part1_example = solve(example_lines[0], 10)
    part1 = solve(lines[0], 40)
    part2 = solve(lines[0], 400000)

    info('part 1')
    info('example  : %s' % (part1_example))
    info('solution : %s' % (part1))

    print

    info('part 2')
    info('solution : %s' % (part2))

class Test(unittest.TestCase):
    # @unittest.skip('skip')
    def test(self):
        self.assertTrue(True)

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
