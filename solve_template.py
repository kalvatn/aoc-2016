#!/usr/bin/env python

import unittest
import sys
import os
import time
# from itertools import permutations
# from itertools import combinations_with_replacement
# from itertools import combinations
# import deque

RUN_TESTS = False
VISUALIZE = False
QUIET = False

def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()
    part1_example = None
    part1 = None

    part2_example = None
    part2 = None


    print 'part 1 example : %s' % (part1_example)
    print 'part 1 : %s' % (part1)
    print 'part 2 example : %s' % (part2_example)
    print 'part 2 : %s' % (part2)

class Test(unittest.TestCase):
    # @unittest.skip('skip')
    def test(self):
        self.assertTrue(True)

def get_input_lines(input_file='input'):
    try:
        return [ line.strip() for line in open(input_file) ]
    except:
        print 'could not read input file %s' % input_file
        return []

def process_args(args):
    if args:
        VISUALIZE = '-v' in args
        QUIET = '-q' in args
        RUN_TESTS = '-t' in args
    if RUN_TESTS:
        args = []
        unittest.main(argv=[sys.argv[0]])

if __name__ == '__main__':
    process_args(sys.argv[1:])
    main()
else:
    process_args(sys.argv[1:])
    main()
