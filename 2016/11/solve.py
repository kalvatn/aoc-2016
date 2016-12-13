#!/usr/bin/env python


import re
import unittest


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
    def __init__(self, floors):
        self.floors = floors

    def is_valid(self):
        for floor in floors:
            chips = [ chip.split('-')[0] for chip in floor if chip.endswith('-microchip') ]
            generators = [ gen.split('-')[0] for gen in floor if gen.endswith('-generator') ]
            for element in chips:
                if element not in generators and len(generators) > 0:
                    return False




class Test(unittest.TestCase):
    def test_parse(self):
        lines = [
'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
'The second floor contains a hydrogen generator.',
'The third floor contains a lithium generator.',
'The fourth floor contains nothing relevant.',
                ]
        # lines = [
# 'The first floor contains a promethium generator and a promethium-compatible microchip.',
# 'The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.',
# 'The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.',
# 'The fourth floor contains nothing relevant.',
        # ]

        parser = InputParser(lines)
        for floor in parser.get_initial_state():
            print floor

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
