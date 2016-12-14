#!/usr/bin/env python

import unittest
import re

from itertools import permutations
from operator import mul

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
        return '%15s (CAP:%2d DUR:%2d FLA:%2d TEX:%2d CAL:%2d)' % (self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)

    def __repr__(self):
        return '%s' % self.name

def get_integer_combinations(number_of_variables, max_range):
    numbers = range(0, max_range + 1)
    return [ combination for combination in permutations(numbers, number_of_variables) if sum(combination) == max_range ]


def zero_if_negative(value):
    return value if value > 0 else 0

def get_optimal_spoon_distribution(ingredients, max_spoons):
    best = None
    number_of_variables = len(ingredients)
    for combination in get_integer_combinations(number_of_variables, max_spoons):
        properties = {
            'capacity' : 0,
            'durability' : 0,
            'flavor' : 0,
            'texture' : 0,
            # 'calories' : 0
        }
        for i in range(0, number_of_variables):
            ingredient = ingredients[i]
            spoons = combination[i]
            properties['capacity'] += (ingredient.capacity * spoons)
            properties['durability'] += (ingredient.durability * spoons)
            properties['flavor'] += (ingredient.flavor * spoons)
            properties['texture'] += (ingredient.texture * spoons)
            # properties['calories'] += (ingredient.calories * spoons)

        factors = [ zero_if_negative(v) for v in properties.values() ]
        product = reduce(mul, factors, 1)
        if best is None or product > best[0]:
            best = (product, combination)
            print best
    return best

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

    part1 = get_optimal_spoon_distribution(ingredients, 100)


    print 'part 1 : %d (%s)' % (part1[0], part1[1])
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
    # with open('example_input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
