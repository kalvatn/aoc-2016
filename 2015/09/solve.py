#!/usr/bin/env python

from stdlib import aoc
import operator

class Location(object):
    def __init__(self, name):
        self.name = name
        self.routes = {}
    def add_route(self, location, distance):
        if location not in self.routes:
            self.routes[location.name] = distance
    def get_routes(self):
        return self.routes
    def get_routes_ordered_by_shortest(self):
        return sorted(self.routes.items(), key=operator.itemgetter(1))

    def get_routes_ordered_by_longest(self):

        shortest = sorted(self.routes.items(), key=operator.itemgetter(1))
        shortest.reverse()
        return shortest

    def __str__(self):
        return '%s - routes : %s' % (self.name, self.routes)
    def __repr__(self):
        return str(self)

class Day9(aoc.Day):
    def __init__(self):
        super(Day9, self).__init__(__file__)

    def run(self):
        lines = self.read_input()
        # print lines
        locations = {}
        for line in lines:
            route, distance = [ x.strip() for x in line.split('=') ]
            start, end = [ x.strip() for x in route.split('to') ]
            # print "start : '%s', end : '%s', distance : '%d'" % (start, end, int(distance))
            if start not in locations:
                locations[start] = Location(start)
            if end not in locations:
                locations[end] = Location(end)

            loc1 = locations[start]
            loc2 = locations[end]
            loc1.add_route(loc2, int(distance))
            loc2.add_route(loc1, int(distance))

        visited = []
        distance = 0
        min_distance = float('inf')
        max_distance = -1
        for loc in locations.values():
            short_distance = self.visit(loc, 0, [], locations)
            min_distance = short_distance if short_distance < min_distance else min_distance

            long_distance = self.visit(loc, 0, [], locations, longest=True)
            max_distance = long_distance if long_distance > max_distance else max_distance

        part1 = min_distance
        part2 = max_distance

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

    def visit(self, start, distance, visited, locations, longest=False):
        visited.append(start.name)
        if len(visited) == len(locations):
            return distance
        routes = start.get_routes_ordered_by_shortest() if not longest else start.get_routes_ordered_by_longest()
        for k in routes:
            if k[0] in visited:
                continue
            distance += k[1]
            return self.visit(locations[k[0]], distance, visited, locations, longest=longest)
        return distance

if __name__ == '__main__':
    Day9().run()
