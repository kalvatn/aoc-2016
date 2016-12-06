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

KEYPAD_PART_TWO = [
    [ '.', '.', '1', '.', '.' ],
    [ '.', '2', '3', '4', '.' ],
    [ '5', '6', '7', '8', '9' ],
    [ '.', 'A', 'B', 'C', '.' ],
    [ '.', '.', 'D', '.', '.' ],
]


def main(lines, keypad, start_row, start_col):
    # print lines
    row = start_row
    col = start_col
    new_row = start_row
    new_col = start_col
    last_position = keypad[row][col]
    code = []
    for line in lines:
        for direction in line:
            if direction in [UP, DOWN]:
                new_row = get_row(row, direction, keypad)
                if not keypad[new_row][col] == '.':
                    row = new_row
            if direction in [LEFT, RIGHT]:
                new_col = get_col(col, direction, keypad)
                if not keypad[row][new_col] == '.':
                    col = new_col
        last_position = keypad[row][col]
        code.append(last_position)

    print ''.join([str(x) for x in code])

def get_row(current, direction, keypad):
    if direction == UP and current > 0:
        return current - 1
    if direction == DOWN and current < len(keypad) - 1:
        return current + 1
    return current


def get_col(current, direction, keypad):
    if direction == LEFT and current > 0:
        return current - 1
    if direction == RIGHT and current < len(keypad) - 1:
        return current + 1
    return current


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    # main(lines, KEYPAD, 1, 1)
    main(lines, KEYPAD_PART_TWO, 2, 0)
