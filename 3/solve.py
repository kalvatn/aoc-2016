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







if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
