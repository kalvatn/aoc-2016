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
        else:
            self.log.setLevel(logging.INFO)

        if self.visualize:
            self.log.setLevel(logging.DEBUG)
            self.log.info('visualize')

        self.log.info('name: %s, loglevel: %s, verbose: %s, visualize: %s' % (
            '/'.join(self.name.split('/')[-3:]),
            self.log.getEffectiveLevel(),
            self.verbose,
            self.visualize))

    def read_input(self, input_file='input'):
        lines = []
        filepath = os.path.join(os.path.dirname(self.name), input_file)
        try:
            self.log.debug("reading input from file '%s'" % (filepath))
            with open(filepath, 'r') as in_file:
                lines = [ line.strip() for line in in_file ]
        except:
            self.log.warn("could not read file '%s'" % (filepath))
        return lines
