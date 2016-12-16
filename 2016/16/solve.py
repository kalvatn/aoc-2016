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
VISUALIZE = True

def invert(a):
    if len(a) == 1:
        return '1' if a == '0' else '0'
    return ''.join([invert(b) for b in a])


def dragon(a):
    b = ''.join(reversed([invert(c) for c in a]))
    return a + '0' + b

def checksum(a):
    c = ''
    for i in range(0, len(a)-1, 2):
        # debug('a1 a1+1 : ' + a[i] + a[i+1])
        if a[i] == a[i+1]:
            c += '1'
        else:
            c += '0'
        # debug('c : ' + c)
    return c if len(c) % 2 != 0 else checksum(c)

def truncate(state, length):
    if len(state) < length:
        raise ValueError('len(%s) < length (%d)' % (state, length))

    return state[0:length]

def get_disk_data(state, length):

    debug(state)
    while len(state) < length:
        state = dragon(state)
        debug(state)
    return truncate(state, length)

def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()

    part1_example = checksum(get_disk_data(example_lines[0], 20),)
    part1 = checksum(get_disk_data(lines[0], 272))

    part2 = checksum(get_disk_data(lines[0], 35651584))

    info('part 1')
    info('example  : %s' % (part1_example))
    info('solution : %s' % (part1))

    print

    info('part 2')
    info('solution : %s' % (part2))

class Test(unittest.TestCase):
    def test_dragon(self):
        self.assertEquals(dragon('1'), '100')
        self.assertEquals(dragon('0'), '001')
        self.assertEquals(dragon('11111'), '11111000000')
        self.assertEquals(dragon('111100001010'), '1111000010100101011110000')


    def test_checksum(self):
        self.assertEquals(checksum('110010110100'), '100')


    def test_truncate(self):
        self.assertEquals(truncate('100', 1), '1')
        self.assertEquals(truncate('101010', 3), '101')
        self.assertEquals(truncate('000111000', 4), '0001')
        self.assertEquals(truncate('111111110', 5), '11111')
        self.assertEquals(len(truncate('10000011110010000111110', 20)), 20)
        self.assertEquals(truncate('10000011110010000111110', 20), '10000011110010000111')

    def test_get_disk_data(self):
        self.assertEquals(get_disk_data('10000', 20), '10000011110010000111')

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
        VERBOSE = True
        args = []
        unittest.main(argv=[sys.argv[0]])
    debug('VERBOSE=%s, VISUALIZE=%s (%s)' % (VERBOSE, VISUALIZE, args))

if __name__ == '__main__':
    process_args(sys.argv[1:])
    main()
else:
    process_args(sys.argv[1:])
    main()
