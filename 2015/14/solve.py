#!/usr/bin/env python

import unittest
import re

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

class Reindeer(object):
    def __init__(self, name, speed, fly_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration

    def __str__(self):
        return '%s %dkm/s for %d, rest %d' % (self.name, self.speed, self.fly_duration, self.rest_duration)

def main(lines):
    part1 = None
    part2 = None

    pattern = re.compile(r'^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.$')
    reindeers = []
    for line in lines:
        match = pattern.match(line)
        name, speed, fly_duration, rest_duration = match.groups()
        reindeers.append(Reindeer(name, int(speed), int(fly_duration), int(rest_duration)))

    for reindeer in reindeers:
        print reindeer

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
