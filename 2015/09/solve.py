#!/usr/bin/env python

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

    def __str__(self):
        return '%s - routes : %s' % (self.name, self.routes)
    def __repr__(self):
        return str(self)

def main(lines):
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
    min_distance = -1
    for loc in locations.values():
        distance = visit(loc, 0, [], locations)
        if min_distance < 0:
            min_distance = distance
        if distance < min_distance:
            min_distance = distance
    part1 = min_distance
    part2 = ''

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def visit(start, distance, visited, locations):
    visited.append(start.name)
    # print 'visited : %s , distance : %d' % (visited, distance)
    if len(visited) == len(locations):
        return distance
    for k in start.get_routes_ordered_by_shortest():
        if k[0] in visited:
            continue
        distance += k[1]
        return visit(locations[k[0]], distance, visited, locations)
    return distance




if __name__ == '__main__':
    test_input = [
        # 'London to Dublin = 464',
        # 'London to Belfast = 518',
        # 'Dublin to Belfast = 141',
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
