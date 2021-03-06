#!/usr/bin/env python

import re

from itertools import permutations
from operator import mul

from stdlib import aoc

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

class Day15(aoc.Day):
    def __init__(self):
        super(Day15, self).__init__(__file__)

    def get_integer_combinations(self, number_of_variables, max_range):
        numbers = range(0, max_range + 1)
        return [ combination for combination in permutations(numbers, number_of_variables) if sum(combination) == max_range ]

    def zero_if_negative(self, value):
        return value if value > 0 else 0

    def get_optimal_spoon_distribution(self, ingredients, max_spoons):
        best = None
        best_calories = None
        number_of_variables = len(ingredients)
        for combination in self.get_integer_combinations(number_of_variables, max_spoons):
            properties = {
                'capacity' : 0,
                'durability' : 0,
                'flavor' : 0,
                'texture' : 0
            }
            calories = 0
            for i in range(0, number_of_variables):
                ingredient = ingredients[i]
                spoons = combination[i]
                properties['capacity'] += (ingredient.capacity * spoons)
                properties['durability'] += (ingredient.durability * spoons)
                properties['flavor'] += (ingredient.flavor * spoons)
                properties['texture'] += (ingredient.texture * spoons)
                calories += (ingredient.calories * spoons)

            factors = [ self.zero_if_negative(v) for v in properties.values() ]
            product = reduce(mul, factors, 1)
            if calories == 500:
                if best_calories is None or product > best_calories[0]:
                    best_calories = (product, combination)

            if best is None or product > best[0]:
                best = (product, combination)
        return [ best, best_calories ]

    def run(self):
        ingredients = []
        for line in self.read_input():
            name, mods = line.split(':')
            mods = [ int(value) for value in [ prop.split()[1] for prop in mods.split(',')] ]
            ingredients.append(Ingredient(name, mods[0], mods[1], mods[2], mods[3], mods[4]))

        for ingredient in ingredients:
            self.log.debug(ingredient)

        best_combo = self.get_optimal_spoon_distribution(ingredients, 100)

        self.log.info('part 1 : %d (%s)' % (best_combo[0][0], best_combo[0][1]))
        self.log.info('part 2 : %d (%s)' % (best_combo[1][0], best_combo[1][1]))

if __name__ == '__main__':
    Day15().run()
