#!/usr/bin/env python


UP    = '^'
DOWN  = 'v'
RIGHT = '>'
LEFT  = '<'

VISITED = {
    (0,0) : 1
}

def main(lines):
    # print VISITED
    directions = lines[0]

    pos_x = 0
    pos_y = 0

    for direction in directions:
    # for direction in '>':
    # for direction in '^>v<':
    # for direction in '^v^v^v^v^v':
        if direction == UP:
            pos_y += 1
        if direction == DOWN:
            pos_y -= 1
        if direction == LEFT:
            pos_x -= 1
        if direction == RIGHT:
            pos_x += 1

        pos = (pos_x, pos_y)
        if pos not in VISITED:
            VISITED[pos] = 0
        VISITED[pos] += 1

    # print VISITED
    houses_with_presents = 0
    for k, v in VISITED.items():
        if v >= 1:
            houses_with_presents += 1
    print houses_with_presents




if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
