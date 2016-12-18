#!/usr/bin/env python

import operator
import re

from stdlib import aoc

class Reindeer(object):
    def __init__(self, name, speed, fly_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self.total_distance = 0

        self.rest_counter = 0
        self.fly_counter = 0
        self.points = 0

    def give_point(self):
        self.points += 1

    def fly(self):
        if self.rest_counter > 0:
            self.rest_counter -= 1
            if self.rest_counter == 0:
                self.fly_counter = 0
        else:
            if self.fly_counter < self.fly_duration:
                self.fly_counter += 1
                self.total_distance += self.speed
            else:
                self.rest_counter = self.rest_duration -1
        # print '%s fly : %d, rest : %d, distance : %d' % (self.name, self.fly_counter, self.rest_counter, self.total_distance)

    def __str__(self):
        return '%10s - %4d km, %4d points' % (self.name, self.total_distance, self.points)
    def __repr__(self):
        return self.name


class Day14(aoc.Day):
    def __init__(self):
        super(Day14, self).__init__(__file__)

    def find_leading(self, reindeers):
        ranking = [ (reindeer, reindeer.total_distance) for reindeer in reindeers ]
        ranking = [ r for r in reversed(sorted(ranking, key=operator.itemgetter(1))) ]
        best = [ranking[0]]
        for tied in ranking[1:]:
            if tied[1] == best[0][1]:
                best.append(tied)
        return best

    def run(self):
        lines = self.read_input()
        part1 = None
        part2 = None

        pattern = re.compile(r'^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.$')
        reindeers = []
        for line in lines:
            match = pattern.match(line)
            name, speed, fly_duration, rest_duration = match.groups()
            reindeers.append(Reindeer(name, int(speed), int(fly_duration), int(rest_duration)))

        for i in range(0, 2503):
            for reindeer in reindeers:
                reindeer.fly()
            for best in self.find_leading(reindeers):
                best[0].give_point()

        best_distance = (0, reindeers[0])
        best_points = (0, reindeers[0])
        for reindeer in reindeers:
            if best_distance[0] < reindeer.total_distance:
                best_distance = (reindeer.total_distance, reindeer)
            if best_points[0] < reindeer.points:
                best_points = (reindeer.points, reindeer)

        for reindeer in reindeers:
            self.log.debug(reindeer)

        part1 = best_distance
        part2 = best_points

        self.log.info('part 1 : %d (%s)' % (part1[0], part1[1]))
        self.log.info('part 2 : %d (%s)' % (part2[0], part2[1]))

if __name__ == '__main__':
    Day14().run()
