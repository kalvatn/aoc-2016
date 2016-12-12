#!/usr/bin/env python

import unittest



class Test(unittest.TestCase):
    def test_part_one_examples(self):
        lines = [
'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
'The second floor contains a hydrogen generator.',
'The third floor contains a lithium generator.',
'The fourth floor contains nothing relevant.',
                ]
        lines = [
'The first floor contains a promethium generator and a promethium-compatible microchip.',
'The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.',
'The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.',
'The fourth floor contains nothing relevant.',
        ]

        import re
        # pattern = re.compile(r'The (first|second|third|fourth) floor contains ((and|,)[\sa]*([\w]+(?:-compatible)? (microchip|generator)))*')
        pattern = re.compile(r'^The (first|second|third|fourth) floor contains (?:a (([\w]+)(?:-compatible)?\s(microchip|generator)[\s]*(and|,)*)|nothing relevant)*\.$')
        for line in lines:
            matches = pattern.findall(line)
            if matches:
                for match in matches:
                    print match
                    # print match.group(0)

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
