#!/usr/bin/env python


import re
import unittest

import unittest
import sys
import os
import time
# from itertools import permutations
# from itertools import combinations_with_replacement
from itertools import combinations
# import deque

VERBOSE = True
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
    def __init__(self, floors, floor_index):
        self.parent = None
        self._floors = [ sorted(floor) for floor in floors ]
        self._current_floor = floor_index

        self.h_score = 0
        self.g_score = float('inf')

    def move_cost(self):
        return 1

    def heuristic(self):
        return len(self.floors) - self.floor_index + len(self.items_on_floor_four())

    @property
    def f_score(self):
        return self.h_score + self.g_score

    @property
    def floors(self):
        return self._floors

    @property
    def floor_index(self):
        return self._current_floor

    def items_on_floor_four(self):
        return set([ item for item in self.floors[3] ])

    def is_valid(self):
        # if len(self.items) != sum(map(len, self.floors)):
        #     return False
        for floor in self.floors:
            chips = [ chip.split('-')[0] for chip in floor if chip.endswith('-microchip') ]
            generators = [ gen.split('-')[0] for gen in floor if gen.endswith('-generator') ]
            for element in chips:
                if element not in generators and len(generators) > 0:
                    return False
        return True

    def __str__(self):
        return 'E%d %s' % (self.floor_index, [ floor for floor in self.floors ])

    def __repr__(self):
        return 'State %d %s' % (self.floor_index, self.floors)

    def print_to_stdout(self):
        print
        for i in range(0, len(self.floors)):
            floor_indicator = 'E%d' % i if self.floor_index == i else str(i)
            print '%2s - %s' % (floor_indicator, self.floors[i])
        print

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.__repr__())


class StateGenerator(object):
    def __init__(self, current):
        self.current = current

    def successors(self):
        floor_index = self.current.floor_index
        floor_state = self.current.floors
        floor_items = self.current.floors[floor_index]

        candidates = set()


        bottom_floor_with_items = 0
        for i in range(0, len(floor_state)):
            if len(floor_state[i]) > 0:
                bottom_floor_with_items = i
                break

        going_up = False

        for i in (1, -1):
            next_floor_index = floor_index + i
            if next_floor_index >= len(floor_state) or next_floor_index < bottom_floor_with_items:
                continue

            if next_floor_index > floor_index:
                going_up = True

            next_floor_items = floor_state[next_floor_index]
            items = floor_items[:]
            combos = list(combinations(items, 1)) + list(combinations(items, 2))

            for combo in combos:
                new_floor_items = [ item for item in floor_items if item not in combo ]
                new_next_floor_items = [ item for item in combo ] + next_floor_items

                new_floor_state = floor_state[:]
                # new_floor_state[floor_index] = new_floor_items
                # new_floor_state[next_floor_index] = new_next_floor_items

                new_floor_state[floor_index] = sorted(new_floor_items)
                new_floor_state[next_floor_index] = sorted(new_next_floor_items)
                new_state = State(new_floor_state, next_floor_index)
                if new_state.is_valid():
                    candidates.add(new_state)
        return candidates

def bfs(start, goal):
    visited = set()
    frontier = set([start])
    steps = 0

    all_items = set([ item for floor in goal.floors for item in floor ])
    current = start
    while len(frontier) > 0:
        new_frontier = set()

        for state in frontier:
            visited.add(state)
            if state.items_on_floor_four() == all_items:
                print 'found goal'
                current = state
                path = []
                path.append(current)
                while current.parent and current.parent != start:
                    path.append(current.parent)
                    current = current.parent
                return path[::-1]
            successors = StateGenerator(state).successors()

            for successor in successors:
                successor.parent = state
                if successor not in visited:
                    new_frontier.add(successor)
        frontier = new_frontier
        steps += 1
        debug('steps : %d frontier %d' % (steps, len(frontier)))
    raise ValueError('could not find path')

def astar(start, goal):
    fringe = set([start])
    closed = set()
    visited = set()

    all_items = set([ item for floor in goal.floors for item in floor ])

    while fringe:
        current = min(fringe, key=lambda state: state.f_score)

        visited.add(current)

        if current.items_on_floor_four() == all_items:
            path = []
            while current.parent and current.parent != start:
                path.append(current.parent)
                current = current.parent
            return path[::-1]
        fringe.remove(current)
        closed.add(current)
        for state in StateGenerator(current).successors():
            visited.add(state)
            if state in closed:
                continue
            state.parent = current
            cost = current.g_score + 1
            if state in fringe:
                if state.g_score > cost:
                    state.g_score = cost
            else:
                state.g_score = state.move_cost()
                state.h_score = state.heuristic()
                fringe.add(state)






def main():
    example_lines = get_input_lines(input_file='example_input')
    lines = get_input_lines()
    initial_state = State(InputParser(example_lines).get_initial_state(), 0)
    all_items = set([ item for floor in initial_state.floors for item in floor ])
    goal_state = State([ [], [], [], [ item for item in all_items ] ], 3)

    info('initial state')
    initial_state.print_to_stdout()
    info('goal state')
    goal_state.print_to_stdout()

    path = bfs(initial_state, goal_state)

    # path = astar(initial_state, goal_state)

    print 'found in %d steps (BFS)' % (len(path))
    path = astar(initial_state, goal_state)
    part1_example = len(path)
    print 'found in %d steps (A*)' % (len(path))
    for path in path:
        print path

    initial_state = State(InputParser(lines).get_initial_state(), 0)
    all_items = set([ item for floor in initial_state.floors for item in floor ])
    goal_state = State([ [], [], [], [ item for item in all_items ] ], 3)

    path = bfs(initial_state, goal_state)
    # path = astar(initial_state, goal_state)

    print 'found in %d steps : %s' % (len(path), path)
    for path in path:
        print path
    part1 = len(path)

    part2_example = None
    part2 = None

    info('part 1')
    info('example  : %d' % (part1_example))
    info('solution : %d' % (part1))

    print

    info('part 2')
    info('example  : %s' % (part2_example))
    info('solution : %s' % (part2))


class Test(unittest.TestCase):
    def setUp(self):
        self.example_lines = get_input_lines(input_file='example_input')
        self.lines = get_input_lines()

    def test_parse(self):
        floors = InputParser(self.example_lines).get_initial_state()
        self.assertEquals(floors[0], ['hydrogen-microchip', 'lithium-microchip'])
        self.assertEquals(floors[1], ['hydrogen-generator'])
        self.assertEquals(floors[2], ['lithium-generator'])
        self.assertEquals(floors[3], [])

        floors = InputParser(self.lines).get_initial_state()
        self.assertEquals(floors[0], ['promethium-generator', 'promethium-microchip'])
        self.assertEquals(floors[1], ['cobalt-generator', 'curium-generator', 'ruthenium-generator', 'plutonium-generator'])
        self.assertEquals(floors[2], ['cobalt-microchip', 'curium-microchip', 'ruthenium-microchip', 'plutonium-microchip'])
        self.assertEquals(floors[3], [])

    def test_state_invalid_mixed_unconnected(self):
        self.assertFalse(State([['promethium-generator', 'cobalt-microchip'], [], [], []], 0).is_valid())
        self.assertFalse(State([['promethium-generator', 'promethium-microchip', 'cobalt-microchip'], [], [], []], 0).is_valid())

    def test_state_valid_mixed_connected(self):
        self.assertTrue(State([['promethium-generator', 'promethium-microchip', 'cobalt-generator', 'cobalt-microchip'], [], [], []], 0).is_valid())

    def test_state_valid_mixed_no_generators(self):
        self.assertTrue(State([['promethium-microchip', 'cobalt-microchip'], [], [], []], 0).is_valid())
        self.assertTrue(State([['promethium-microchip', 'cobalt-microchip', 'whatever-microchip'], [], [], []], 0).is_valid())

    def test_state_valid_mixed_generators(self):
        self.assertTrue(State([['promethium-generator', 'cobalt-generator', 'whatever-generator'], [], [], []], 0).is_valid())
        self.assertTrue(State([['promethium-generator', 'promethium-microchip', 'cobalt-generator', 'whatever-generator'], [], [], []], 0).is_valid())

    def test_state_is_valid_for_inputs(self):
        self.assertTrue(State(InputParser(self.example_lines).get_initial_state(), 0).is_valid())
        self.assertTrue(State(InputParser(self.lines).get_initial_state(), 0).is_valid())

    def test_state_generator(self):
        initial_state = State(InputParser(self.example_lines).get_initial_state(), 0)
        successors = StateGenerator(initial_state).successors()

        print 'current'
        initial_state.print_to_stdout()

        print 'possible'

        for successor in successors:
            successor.print_to_stdout()
        if len(successors) == 1:
            for successor in successors:
                for x in StateGenerator(successor).successors():
                    successor.print_to_stdout()
                break

        all_items = set([ item for floor in initial_state.floors for item in floor ])
        print 'all items : %s' % all_items
        self.assertNotEquals(initial_state.items_on_floor_four(), all_items)

    def test_state_equality(self):
        s1 = State([[], [], [], []], 0)
        s2 = State([[], [], [], []], 0)
        self.assertEquals(s1, s2)

        s1 = State([['x-generator'], [], [], []], 0)
        s2 = State([['x-generator'], [], [], []], 0)
        self.assertEquals(s1, s2)

        seen = set()
        seen.add(s1)
        seen.add(s2)

        self.assertEquals(len(seen), 1)
        s3 = State([['x-generator'], [], [], []], 1)
        seen.add(s3)
        self.assertEquals(len(seen), 2)
        seen.add( State([['x-generator'], [], [], []], 1))
        self.assertEquals(len(seen), 2)

        seen.add( State([['x-generator'], [], [], []], 2))
        seen.add( State([['x-generator'], [], [], []], 3))
        self.assertEquals(len(seen), 4)

def get_input_lines(input_file='input'):
    try:
        return [ line.strip() for line in open(input_file) ]
    except:
        warn('could not read input file %s' % input_file)
        return []

def debug(thing):
    if VERBOSE:
        _print(str(thing), color='green')

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
        args = [ '-v' ]
        VERBOSE = True
        unittest.main(argv=[sys.argv[0]] + args)
    debug('VERBOSE=%s, VISUALIZE=%s (%s)' % (VERBOSE, VISUALIZE, args))

if __name__ == '__main__':
    process_args(sys.argv[1:])
    main()
else:
    process_args(sys.argv[1:])
    main()
