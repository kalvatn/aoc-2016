#!/usr/bin/env python

def main(lines):
    possible = 0
    for line in lines:
        sides = [int(x) for x in line.strip().split()]
        largest = sides.pop(sides.index(max(sides)))
        sum_smaller = sum(sides)
        if sum_smaller > largest:
            possible += 1
    print possible

def part_two(lines):
    # lines = [
# '101 301 501',
# '102 302 502',
# '103 303 503',
# '201 401 601',
# '202 402 602',
# '203 403 603',
    # ]
    possible = 0

    by_columns = group_by_columns(lines)
    for col in by_columns:

        for sides in group_by_hundreds(col):
            largest = sides.pop(sides.index(max(sides)))
            sum_smaller = sum(sides)
            if sum_smaller > largest:
                possible += 1
    print possible

def group_by_hundreds(column):
    in_threes = []
    while len(column) > 0:
        sides = [column.pop() for x in range(0,3)]
        in_threes.append(sides)
    return in_threes



def group_by_columns(lines):
    by_columns = [[],[],[]]
    for line in lines:
        col1, col2, col3 = [ int(x) for x in line.strip().split() ]
        by_columns[0].append(col1)
        by_columns[1].append(col2)
        by_columns[2].append(col3)

    return by_columns

if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    print "part 1"
    main(lines)
    print "part 2"
    part_two(lines)
