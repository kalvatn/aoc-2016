#!/usr/bin/env python

import unittest
import re

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass


class Person(object):
    def __init__(self, name):
        self.name = name
        self.bad = {}
        self.good = {}

    def add_negative(self, name, weight):
        self.bad[name] = weight

    def add_positive(self, name, weight):
        self.good[name] = weight

    def __str__(self):
        return '%s, good : %s, bad : %s' % (self.name, self.good, self.bad)

    def __repr__(self):
        return '%s' % (self.name)


def main(lines):
    part1 = None
    part2 = None

    pattern = re.compile(r'^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.$')
    persons = {}

    for line in lines:
        match = pattern.match(line)
        if match:
            subject, gainlose, weight, neighbour = match.groups()
            if subject not in persons:
                persons[subject] = Person(subject)

            if gainlose == 'gain':
                persons[subject].add_positive(neighbour, int(weight))
            else:
                persons[subject].add_negative(neighbour, int(weight) * -1)

    for k, v in persons.items():
        print v

    part1 = part_one(persons.values())

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def part_one(persons):
    from itertools import permutations

    # print persons
    best_sum = None
    for perm in permutations(persons):
        perm_sum = 0
        for i in range(0, len(perm)):
            l = i - 1
            r = i + 1 if i + 1 < len(perm) else 0
            left = perm[l]
            current = perm[i]
            right = perm[r]
            if right.name in current.good:
                perm_sum += current.good[right.name]
            if right.name in current.bad:
                perm_sum += current.bad[right.name]

            if left.name in current.good:
                perm_sum += current.good[left.name]
            if left.name in current.bad:
                perm_sum += current.bad[left.name]
        best_sum = perm_sum if best_sum is None or best_sum < perm_sum else best_sum
        if perm_sum > 0:
            print '%s : %d' % (perm, perm_sum)
    return best_sum

if __name__ == '__main__':
    # unittest.main()
    lines = []
    # with open('input') as file:
    with open('example_input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
