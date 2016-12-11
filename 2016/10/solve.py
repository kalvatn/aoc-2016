#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        cases = [
            { 'input' : '', 'expect' : '' },
            { 'input' : '', 'expect' : '' },
            { 'input' : '', 'expect' : '' }
        ]
        for case in cases:
            case_input = case['input']
            case_expect = case['expect']
            actual = part_one(case_input)
            self.assertEquals(actual, case_expect, "part_one('%s'), expected '%s', was '%s'" % (case_input, case_expect, actual))

    def test_part_two_examples(self):
        cases = [
            { 'input' : '', 'expect' : '' },
            { 'input' : '', 'expect' : '' },
            { 'input' : '', 'expect' : '' }
        ]

        for case in cases:
            case_input = case['input']
            case_expect = case['expect']
            actual = part_two(case_input)
            self.assertEquals(actual, case_expect, "part_two('%s'), expected '%s', was '%s'" % (case_input, case_expect, actual))

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
