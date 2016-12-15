#!/usr/bin/env python

import unittest
import re

UNKNOWN = -1

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

class Aunt(object):
    def __init__(self, number, props):
        self.number = number
        self.props = props

    def __str__(self):
        return 'Sue %d - %s' % (self.number, self.props)

    def __repr__(self):
        return str(self)


def main(lines):
    target_props = {
        'children' : 3,
        'cats' : 7,
        'samoyeds' : 2,
        'pomeranians' : 3,
        'akitas' : 0,
        'vizslas' : 0,
        'goldfish' : 5,
        'trees' : 3,
        'cars' : 2,
        'perfumes' : 1
    }
    target = Aunt(UNKNOWN, target_props)
    pattern = re.compile(r'(?:Sue (\d+):)* (children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+),?')
    aunts = []
    for line in lines:
        props = {
            'children' : UNKNOWN,
            'cats' : UNKNOWN,
            'samoyeds' : UNKNOWN,
            'pomeranians' : UNKNOWN,
            'akitas' : UNKNOWN,
            'vizslas' : UNKNOWN,
            'goldfish' : UNKNOWN,
            'trees' : UNKNOWN,
            'cars' : UNKNOWN,
            'perfumes' : UNKNOWN
        }
        matches = pattern.finditer(line)
        number = None
        for match in matches:
            aunt_number, prop_type, prop_count = match.groups()
            if aunt_number is not None:
                number = int(aunt_number)
            props[prop_type] = int(prop_count)
        aunts.append(Aunt(number, props))

    part1_candidates = []
    filtered = []
    for aunt in aunts:
        is_candidate = False
        for k, v in target_props.items():
            if aunt.props[k] != UNKNOWN:
                if aunt.props[k] != v:
                    filtered.append(aunt)
                    break
                else:
                    is_candidate = True
            else:
                is_candidate = True
        if aunt not in filtered and is_candidate:
            part1_candidates.append(aunt)



    print part1_candidates
    part1 = part1_candidates[0].number
    part2 = None
    print 'part 1 : %d' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
