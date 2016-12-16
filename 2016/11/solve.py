#!/usr/bin/env python


import re
import unittest

import unittest
import sys
import os
import time
from itertools import permutations
# from itertools import combinations_with_replacement
# from itertools import combinations
# import deque

VERBOSE = False
RUN_TESTS = False
VISUALIZE = False


class InputParser(object):
    def __init__(self, lines):
        self.lines = lines
        self.floors = [ [], [], [], [] ]
        self.components = []
        self.parse()

    def parse(self):
        pattern = re.compile(r'(?:The (first|second|third|fourth) floor contains)*(?:,?\s(?:and )?a\s([\w]+)(?:-compatible)?\s(microchip|generator))\.*')
        for line in self.lines:
            for match in pattern.finditer(line):
                element = match.groups()[1]
                part = match.groups()[2]
                component = '%s-%s' % (element, part)

                self.components.append(component)

                if match.groups()[0]:
                    floor = match.groups()[0]

                if floor == 'first':
                    self.floors[0].append(component)
                elif floor == 'second':
                    self.floors[1].append(component)
                elif floor == 'third':
                    self.floors[2].append(component)
                elif floor == 'fourth':
                    self.floors[3].append(component)

    def get_initial_state(self):
        return self.floors

    def get_components(self):
        return self.components

class State(object):
    def __init__(self, floors, current_floor):
        self._floors = floors
        self._current_floor = current_floor

    @property
    def floors(self):
        return self._floors

    @property
    def current_floor(self):
        return self._current_floor

    def is_valid(self):
        for floor in self.floors:
            chips = [ chip.split('-')[0] for chip in floor if chip.endswith('-microchip') ]
            generators = [ gen.split('-')[0] for gen in floor if gen.endswith('-generator') ]
            for element in chips:
                if element not in generators and len(generators) > 0:
                    return False
        return True

class StateGenerator(object):
    def __init__(self, current):
        self._current = current
        self._successors = []

    @property
    def current(self):
        return self._current

    @property
    def successors(self):
        return self._successors

    def generate_successors(self):
        states = []
        current_floor = self.current.current_floor
        current_floors = self.current.floors
        can_go_down = current_floor > 0
        can_go_up = current_floor < 3

        if can_go_up:
            floors = [ [], [], [], [] ]
            for i in range(current_floor, len(current_floors) - 1):
                candidates = [ State(x, i) for x in permutations(current_floors) ]
                states += [ state for state in candidates if state.is_valid() ]

        if can_go_down:
            floors = [ [], [], [], [] ]
            for i in range(current_floor, 0, -1):
                candidates = [ State(x, i) for x in permutations(current_floors) ]
                states += [ state for state in candidates if state.is_valid() ]

        self._successors = states





def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()
    part1_example = None
    part1 = None

    part2_example = None
    part2 = None

    info('part 1')
    info('example  : %s' % (part1_example))
    info('solution : %s' % (part1))

    print

    info('part 2')
    info('example  : %s' % (part2_example))
    info('solution : %s' % (part2))


class Test(unittest.TestCase):
    def setUp(self):
        self.lines = [
'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
'The second floor contains a hydrogen generator.',
'The third floor contains a lithium generator.',
'The fourth floor contains nothing relevant.',
                ]

        # self.lines = [
# 'The first floor contains a hydrogen-compatible microchip and a lithium microchip.',
# 'The second floor contains a hydrogen generator.',
# 'The third floor contains a lithium generator.',
# 'The fourth floor contains nothing relevant.',
        #         ]

        # self.lines = [
# 'The first floor contains a promethium generator and a promethium-compatible microchip.',
# 'The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.',
# 'The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.',
# 'The fourth floor contains nothing relevant.',
        # ]

    def test_parse(self):
        parser = InputParser(self.lines)
        for floor in parser.get_initial_state():
            print floor

    def test_state(self):
        floors = InputParser(self.lines).get_initial_state()
        state = State(floors, 0)
        print state.is_valid()

    def test_state_generator(self):
        floors = InputParser(self.lines).get_initial_state()
        state = State(floors, 0)
        gen = StateGenerator(state)
        gen.generate_successors()
        i = 0
        for state in gen.successors:
            print i
            for floor in state.floors:
                print floor
            i += 1


    def test_part_two_examples(self):
        pass


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
