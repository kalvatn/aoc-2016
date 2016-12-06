#!/usr/bin/env python


UP    = '^'
DOWN  = 'v'
RIGHT = '>'
LEFT  = '<'

PART_ONE_VISITED = {
    (0,0) : 1
}
SANTA_VISITED = {
    (0,0) : 1
}
ROBOT_VISITED = {
    (0,0) : 1
}

ALL = 'all'
SANTA = 'santa'
ROBOT = 'robot'

def main(lines):
    # lines = [
    #     # '^v',
    #     # '^>v<',
    #     '^v^v^v^v^v'
    # ]
    directions = lines[0]

    pos = {
        SANTA : [0, 0],
        ROBOT : [0, 0],
        ALL : [0,0]
    }

    turn = SANTA
    for direction in directions:
        x_change = 0
        y_change = 0
        if direction in [ UP, DOWN ]:
            y_change = 1 if direction == UP else -1
        if direction in [ LEFT, RIGHT ]:
            x_change = 1 if direction == RIGHT else -1

        all_pos = (pos[ALL][0] + x_change, pos[ALL][1] + y_change)
        turn_pos = (pos[turn][0] + x_change, pos[turn][1] + y_change)

        pos[ALL] = all_pos
        pos[turn] = turn_pos

        # print '%s - %s' % (ALL, all_pos)
        # print '%s - %s' % (turn, turn_pos)

        if all_pos not in PART_ONE_VISITED:
            PART_ONE_VISITED[all_pos] = 0
        PART_ONE_VISITED[all_pos] += 1

        v = SANTA_VISITED if turn == SANTA else ROBOT_VISITED

        if turn_pos not in v:
            v[turn_pos] = 0
        v[turn_pos] += 1
        turn = ROBOT if turn == SANTA else SANTA

    part_two_visited = set()
    houses_with_presents = 0
    for k, v in PART_ONE_VISITED.items():
        if v >= 1:
            houses_with_presents += 1
    for k, v in SANTA_VISITED.items():
        if v >= 1:
            part_two_visited.add(k)
    for k, v in ROBOT_VISITED.items():
        if v >= 1:
            part_two_visited.add(k)
    # print part_two_visited

    print 'part 1 : %d' % houses_with_presents
    print 'part 2 : %d' % len(part_two_visited)




if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
