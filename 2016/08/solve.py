#!/usr/bin/env python

from collections import deque


ON  = 1
OFF = 0
# WIDTH  = 7
# HEIGHT = 3

WIDTH  = 50
HEIGHT = 6
SCREEN = [deque([ OFF for x in range(WIDTH)]) for y in range(HEIGHT)]


CREATE_RECT = 'rect'
ROTATE_ROW  = 'rotate row y='
ROTATE_COL  = 'rotate column x='

def main(lines):
    print_screen()

    for line in lines:
        # print line
        if line.startswith(CREATE_RECT):
            width, height = [ int(x) for x in line.split(CREATE_RECT)[1].split('x') ]
            create_rect(width, height)
        elif line.startswith(ROTATE_ROW):
            row, by = [ int(x) for x in line.split(ROTATE_ROW)[1].split('by') ]
            rotate_row(row, by)
        elif line.startswith(ROTATE_COL):
            col, by = [ int(x) for x in line.split(ROTATE_COL)[1].split('by') ]
            rotate_col(col, by)
        # print_screen()



    print_screen()


    part1 = count_on()
    part2 = ''

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)



def create_rect(width, height):
    print '%s %dx%d' % (CREATE_RECT, width, height)
    for y in range(0, width):
        for x in range(0, height):
            SCREEN[x][y] = ON

def rotate_row(row, by):
    print '%s %d by %d' % (ROTATE_ROW, row, by)
    SCREEN[row].rotate(by)

def rotate_col(col, by):
    print '%s %d by %d' % (ROTATE_COL, col, by)
    items = deque([ SCREEN[y][col] for y in range(0, HEIGHT)])
    for y in range(0, HEIGHT):
        items.append(SCREEN[y][col])
    items.rotate(by)
    for y in range(0, HEIGHT):
        SCREEN[y][col] = items[y]


def print_screen():
    for row in SCREEN:
        print ' '.join([ str(x) for x in row])

def count_on():
    count = 0
    for row in SCREEN:
        count += sum([ x for x in row])
    return count




if __name__ == '__main__':
    test_input = [
        # 'rect 3x2',
        # 'rotate column x=1 by 1',
        # 'rotate row y=0 by 4',
        # 'rotate column x=1 by 1'
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
