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

VISITED = {
    (0,0) : 0
}





def main(lines):
    # print lines
    # lines = [
    #     'R8, R4, R4, R8'
    # ]

    directions = []
    for line in lines:
        for direction in line.split(','):
            directions.append(direction.strip())

    # print directions

    pos_x = 0
    pos_y = 0
    facing = 'N'
    for entry in directions:
        direction = entry[0]
        count = int(entry[1::])
        # print '%s %d' % (direction, count)

        pos = (pos_x, pos_y)
        old_facing = facing
        facing = new_facing(old_facing, direction)

        if facing == EAST:
            for i in range(0, count):
                pos_x += 1
                visit(pos_x, pos_y)

        if facing == WEST:
            for i in range(0, count):
                pos_x -= 1
                visit(pos_x, pos_y)

        if facing == NORTH:
            for i in range(0, count):
                pos_y += 1
                visit(pos_x, pos_y)

        if facing == SOUTH:
            for i in range(0, count):
                pos_y -= 1
                visit(pos_x, pos_y)

        COUNTS[facing] += count


        # print 'was facing %s, direction %s, now facing %s' % (old_facing, direction, facing)

    # print COUNTS
    vertical= math.fabs(COUNTS[NORTH] - COUNTS[SOUTH])
    horizontal = math.fabs(COUNTS[EAST] - COUNTS[WEST])
    # print "vertical : %s, horizontal %d" % (vertical, horizontal)
    print "%d" % (vertical + horizontal)


def visit(pos_x, pos_y):
    pos = (pos_x, pos_y)
    if pos not in VISITED:
        VISITED[pos] = 0
    VISITED[pos] += 1
    if VISITED[pos] >= 2:
        print "FIRST TWICE : %d, %d" % (pos_x, pos_y)
        vertical= math.fabs(pos_y)
        horizontal = math.fabs(pos_x)
        # print "vertical : %s, horizontal %d" % (vertical, horizontal)
        print "first visited blocks away : %d" % (vertical + horizontal)

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
