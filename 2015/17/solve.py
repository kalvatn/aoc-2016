#!/usr/bin/env python

import unittest
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import combinations

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

def get_combinations(container_sizes, liters, minimum_combo_size=False):
    total = []
    i = 1
    minimum_combo = None
    while True:
        combos = [ combination for combination in combinations(container_sizes, i) if sum(combination) == liters ]
        if not combos and i > 10:
            break
        for combo in combos:
            if minimum_combo is None or len(combo) < minimum_combo:
                minimum_combo = len(combo)
            total.append(combo)
        i += 1
    if minimum_combo_size:
        minimum_total = []
        for combo in total:
            if len(combo) == minimum_combo:
                minimum_total.append(combo)
        return minimum_total
    else:
        return total



def main(lines):
    # container_sizes = [ 20, 15, 10, 5, 5 ]
    # part1 = len(get_combinations(container_sizes, 25))
    # part2 = len(get_combinations(container_sizes, 25, minimum_combo_size=True))

    container_sizes = [ int(line) for line in lines ]
    part1 = len(get_combinations(container_sizes, 150))
    part2 = len(get_combinations(container_sizes, 150, minimum_combo_size=True))

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
