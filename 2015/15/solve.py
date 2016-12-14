#!/usr/bin/env python

import unittest
import re

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return '%10s (CAP:%2d DUR:%2d FLA:%2d TEX:%2d CAL:%2d)' % (self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)

    def __repr__(self):
        return '%s' % self.name

def main(lines):
    part1 = None
    part2 = None

    ingredients = []
    for line in lines:
        name, mods = line.split(':')
        mods = [ int(value) for value in [ prop.split()[1] for prop in mods.split(',')] ]
        ingredients.append(Ingredient(name, mods[0], mods[1], mods[2], mods[3], mods[4]))

    for ingredient in ingredients:
        print ingredient


    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    # with open('input') as file:
    with open('example_input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
