#!/usr/bin/env python

# PUZZLE_INPUT = 10

PUZZLE_INPUT = 1350

def is_clear(x, y):
    out = '(%d, %d)' % (x, y)
    out += ': .' if '{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + PUZZLE_INPUT).count('1') % 2 == 0 else '#'
    print out
    return '{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + PUZZLE_INPUT).count('1') % 2 == 0

def bfs(start, goal):
    visited = set([start])
    frontier = set([start])

    steps = 0

    part1 = None
    part2 = None
    while part1 is None or part2 is None:
        new_frontier = set()
        for point in frontier:
            for x, y in [ (point[0] + dx, point[1] + dy) for dx,dy in [ (1, 0), (-1, 0), (0, 1), (0, -1) ] ]:
                if x < 0 or y < 0 or (x, y) in visited or not is_clear(x, y):
                    # print 'skipping (%d, %d) : clear : %s, is visited : %s' % (x, y, is_clear(x, y), (x,y) in visited)
                    continue
                visited.add((x,y))
                new_frontier.add((x,y))
            print '(%d, %d)' % (point)
        frontier = new_frontier
        steps += 1

        if goal in frontier:
            part1 = steps

        if steps == 50:
            part2 = len(visited)

    print part1
    print part2


def main():
    # bfs((1, 1), (7, 4))

    bfs((1, 1), (31, 39))


if __name__ == '__main__':
    main()
