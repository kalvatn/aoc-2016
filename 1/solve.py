#!/usr/bin/env python

import math


NORTH = 'N'
SOUTH = 'S'
EAST  = 'E'
WEST  = 'W'

RIGHT = 'R'
LEFT  = 'L'

COUNTS = {
    NORTH : 0,
    SOUTH : 0,
    EAST  : 0,
    WEST  : 0
}



def main(lines):
    # print lines

    directions = []
    for line in lines:
        for direction in line.split(','):
            directions.append(direction.strip())

    # print directions
    facing = 'N'
    for entry in directions:
        direction = entry[0]
        count = int(entry[1::])
        # print '%s %d' % (direction, count)

        old_facing = facing
        facing = new_facing(old_facing, direction)
        COUNTS[facing] += count

        # print 'was facing %s, direction %s, now facing %s' % (old_facing, direction, facing)

    # print COUNTS
    vertical= math.fabs(COUNTS[NORTH] - COUNTS[SOUTH])
    horizontal = math.fabs(COUNTS[EAST] - COUNTS[WEST])
    # print "vertical : %s, horizontal %d" % (vertical, horizontal)
    print "%d" % (vertical + horizontal)


def new_facing(current, direction):
    if current == NORTH:
        if direction == LEFT:
            return WEST
        if direction == RIGHT:
            return EAST
    if current == SOUTH:
        if direction == LEFT:
            return EAST
        if direction == RIGHT:
            return WEST
    if current == EAST:
        if direction == LEFT:
            return NORTH
        if direction == RIGHT:
            return SOUTH
    if current == WEST:
        if direction == LEFT:
            return SOUTH
        if direction == RIGHT:
            return NORTH



if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
