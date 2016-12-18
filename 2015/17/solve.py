#!/usr/bin/env python

from itertools import permutations
from itertools import combinations_with_replacement
from itertools import combinations

from stdlib import aoc

class Day17(aoc.Day):
    def __init__(self):
        super(Day17, self).__init__(__file__)

    def get_combinations(self, container_sizes, liters, minimum_combo_size=False):
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

    def run(self):
        lines = self.read_input()

        container_sizes = [ int(line) for line in lines ]
        part1 = len(self.get_combinations(container_sizes, 150))
        part2 = len(self.get_combinations(container_sizes, 150, minimum_combo_size=True))

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

if __name__ == '__main__':
    Day17().run()
