#!/usr/bin/env python

import unittest
import json

from stdlib import aoc

class Day12(aoc.Day):
    def __init__(self):
        super(Day12, self).__init__(__file__)

    def get_number_sum(self, data, ignore=None):
        number_sum = 0
        try:
            number_sum += int(data)
        except:
            if isinstance(data, list):
                for item in data:
                    number_sum += self.get_number_sum(item, ignore=ignore)
            elif isinstance(data, dict):
                if ignore and ignore in data.values():
                    pass
                else:
                    number_sum += self.get_number_sum(data.values(), ignore=ignore)
            else:
                pass
        return number_sum

    def run(self):
        lines = self.read_input()
        json_data = json.loads(''.join(lines))

        part1 = self.get_number_sum(json_data)
        part2 = self.get_number_sum(json_data, ignore='red')

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

if __name__ == '__main__':
    Day12().run()
