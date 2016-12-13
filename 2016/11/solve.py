#!/usr/bin/env python


import re
import unittest
import itertools


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
                candidates = [ State(x, i) for x in itertools.permutations(current_floors) ]
                states += [ state for state in candidates if state.is_valid() ]

        if can_go_down:
            floors = [ [], [], [], [] ]
            for i in range(current_floor, 0, -1):
                candidates = [ State(x, i) for x in itertools.permutations(current_floors) ]
                states += [ state for state in candidates if state.is_valid() ]

        self._successors = states



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

def main(lines):
    print lines

    puzzle_input = parse_lines(lines)

    part1 = part_one(puzzle_input)
    part2 = part_two(puzzle_input)

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def part_one(puzzle_input):
    return ''

def part_two(puzzle_input):
    return ''


if __name__ == '__main__':
    unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
