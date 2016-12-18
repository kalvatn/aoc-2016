#!/usr/bin/env python

import unittest
import sys
import os
import time
from collections import deque

from itertools import permutations
from itertools import combinations_with_replacement
from itertools import combinations

import logging

from stdlib import logutils

VERBOSE = False
RUN_TESTS = False
VISUALIZE = False

class Day(object):
    def __init__(self, name, verbose=False, visualize=False):
        self.name = name
        self.verbose = verbose
        self.visualize = visualize
        self.log = logging.getLogger(name)
        self.log.addHandler(logutils.ColorizingStreamHandler())

        if sys.argv:
            args = sys.argv[1:]
            self.visualize = '--visualize' in args
            self.verbose = '--verbose' in args or '-v' in args

        if self.verbose:
            self.log.setLevel(logging.DEBUG)
            self.log.info('loglevel DEBUG')

        if self.visualize:
            self.log.setLevel(logging.DEBUG)
            self.log.info('visualize')

    @staticmethod
    def create_from_args(name, args):
        visualize = '--visualize' in args
        verbose = '--verbose' in args or '-v' in args
        return Day(name, verbose, visualize)


    def read_input(self, input_file='input'):
        lines = []
        filepath = os.path.join(os.path.dirname(self.name), input_file)
        print filepath
        try:
            with open(filepath, 'r') as in_file:
                lines = [ line.strip() for line in in_file ]
        except:
            self.log.warn("could not read input file '%s'" % input_file)
        return lines

    def run(self):
        self.read_input(input_file='example_input')
        part1_example = None
        part1 = None

        part2_example = None
        part2 = None

        self.log.info('part 1')
        self.log.info('example  : %s' % (part1_example))
        self.log.info('solution : %s' % (part1))

        print

        self.log.info('part 2')
        self.log.info('example  : %s' % (part2_example))
        self.log.info('solution : %s' % (part2))

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

if __name__ == '__main__':
    Day.create_from_args('template', sys.argv[1:]).run()
