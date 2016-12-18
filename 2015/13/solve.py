#!/usr/bin/env python

import unittest
import re

from stdlib import aoc

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

class Day13(aoc.Day):
    def __init__(self):
        super(Day13, self).__init__(__file__)

    def run(self):
        part1 = None
        part2 = None

        pattern = re.compile(r'^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.$')
        persons = {}

        for line in self.read_input():
            match = pattern.match(line)
            if match:
                subject, gainlose, weight, neighbour = match.groups()
                if subject not in persons:
                    persons[subject] = Person(subject)

                if gainlose == 'gain':
                    persons[subject].add_positive(neighbour, int(weight))
                else:
                    persons[subject].add_negative(neighbour, int(weight) * -1)

        part1 = self.find_best_arrangement(persons.values())
        me = Person('Jon Terje')
        for person in persons.values():
            me.good[person.name] = 0
            me.bad[person.name] = 0
            person.good[me.name] = 0
            person.bad[me.name] = 0

        persons[me.name] = me

        part2 = self.find_best_arrangement(persons.values())

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

    def find_best_arrangement(self, persons):
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
            # if perm_sum > 0:
            #     print '%s : %d' % (perm, perm_sum)
        return best_sum

if __name__ == '__main__':
    Day13().run()
