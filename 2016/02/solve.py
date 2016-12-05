#!/usr/bin/env python

UP      = 'U'
DOWN    = 'D'
LEFT    = 'L'
RIGHT   = 'R'

KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def main(lines):
    # print lines
    row = 1
    col = 1
    last_position = KEYPAD[row][col]
    code = []
    for line in lines:
        for direction in line:
            if direction in [UP, DOWN]:
                row = get_row(row, direction)
            if direction in [LEFT, RIGHT]:
                col = get_col(col, direction)
        last_position = KEYPAD[row][col]
        code.append(last_position)
    print ''.join([str(x) for x in code])


def get_row(current, direction):
    if direction == UP and current > 0:
        return current - 1
    if direction == DOWN and current < 2:
        return current + 1
    return current


def get_col(current, direction):
    if direction == LEFT and current > 0:
        return current - 1
    if direction == RIGHT and current < 2:
        return current + 1
    return current


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
