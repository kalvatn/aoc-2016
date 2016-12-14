#!/usr/bin/env python

import unittest
import time
from collections import deque

WALL='#'
OPEN='.'
STEP_INTERVAL_SECONDS = 0.05

class Node(object):
    def __init__(self, value, x, y, parent=None):
        """
        f(n) = g(n) + h(n)

        where n is the last node on the path, g(n) is the cost of the path from
        the start node to n, and h(n) is a heuristic that estimates the cost of
        the cheapest path from n to the goal.
        """

        self.value = value
        self.parent = parent

        self.x = x
        self.y = y

        self.g_score = 0
        self.h_score = 0

    def get_move_cost(self, node):
        return 1

    def get_f_score(self):
        return self.g_score + self.h_score

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return '(%d, %d) - %s' % (self.x, self.y, self.value)

    def __repr__(self):
        return str(self)



class AStar(object):
    def __init__(self, table):
        self.table = table
        self.open = set()
        self.closed  = set()
        self.nodes = [ [ Node(table[x][y], x, y) for y in range(0, len(table)) ] for x in range(0, len(table))]

    def is_valid_point(self, point):
        x, y = point
        valid = x >= 0 and x < len(self.table) and y >= 0 and y < len(self.table) and self.nodes[x][y].value != WALL
        print 'point %s valid : %s' % (point, valid)
        return valid

    def get_neighbours(self, node):
        x, y = node.x, node.y
        left = (x-1, y)
        right = (x+1, y)
        up = (x, y-1)
        down = (x, y+1)
        return [ self.nodes[point[0]][point[1]] for point in [ left, right, up, down ] if self.is_valid_point(point) ]

    def get_manhattan_distance(self, node, goal):
        return abs(goal.x - node.x) + abs(goal.y - node.y)

    def search(self, start_point, goal_point, debug=False):
        start = self.nodes[start_point[0]][start_point[1]]
        goal = self.nodes[goal_point[1]][goal_point[0]]
        # print 'start : %s' % start
        # print 'goal : %s' % goal
        current = start
        self.open.add(current)
        followed_path = []
        visited = set()
        visited.add((start.x, start.y))

        steps = 0
        while self.open:
            current = min(self.open, key=lambda node: node.get_f_score())
            # current = self.open.

            print 'step %d, current : %s, visited : %d' % (steps, (current.x, current.y), len(visited) )
            visited.add((current.x, current.y))

            if current == goal:
                path = []
                while current.parent:
                    path.append((current.x, current.y))
                    current = current.parent
                path.append((current.x, current.y))
                path = path[::-1]

                if debug:
                    print_map(self.table, path)
                return path

            self.open.remove(current)
            self.closed.add(current)

            for node in self.get_neighbours(current):
                # print 'neigbour %s' % node
                visited.add((node.x, node.y))
                # print len(visited)
                if node in self.closed:
                    continue
                node.set_parent(current)
                cost = current.g_score + current.get_move_cost(node)
                if node in self.open:
                    if node.g_score > cost:
                        node.g_score = cost
                else:
                    node.g_score = cost
                    node.h_score = self.get_manhattan_distance(node, goal)
                    self.open.add(node)

            steps += 1
            if steps == 50:
                print 'visited after %d steps : %d' % (steps, len(visited))

            if debug:
                followed_path.append((current.x, current.y))
                print_map(self.table, followed_path)
                time.sleep(STEP_INTERVAL_SECONDS)
        raise ValueError('no valid path found')

def formula(x, y):
    return x*x + 3*x + 2*x*y + y + y*y

def calc_value(x, y, magic_number):
    return formula(x, y) + magic_number

def binary_value(x, y, magic_number):
    return '{0:b}'.format(calc_value(x, y, magic_number))

def get_map_value(x, y, magic_number):
    binary = str(binary_value(x, y, magic_number))
    if binary.count('1') % 2 == 0:
        return OPEN
    return WALL


def print_map(table, path=[]):
    header = '  '
    i = 0
    for x in range(0, len(table[0])):
        i = 0 if x % 10 == 0 else i + 1
        header += '%d' % i

    print header
    for x in range(0, len(table)):
        row = '%2d ' % (x)
        for y in range(0, len(table[x])):
            if (x, y) in path:
                CSI = "\x1B["
                indicator = CSI + "31;40m" + '.' + CSI + "0m"
                if (x, y) == path[0]:
                    indicator = 'S'

                if (x, y) == path[-1]:
                    indicator = 'G'
                row += '%s' % (indicator)
            else:
                row += '%s' % (table[x][y])
        print row



def main(lines):
    width = 50
    height = 45
    # magic_number = 10
    magic_number = int(lines[0])
    table = [[get_map_value(x, y, magic_number) for x in range(0,width)] for y in range(0, height)]
    # print_map(table)

    astar = AStar(table)
    # path = astar.search((1, 1), (7,4))
    # path = astar.search((1, 1), (7,4), True)
    # path = astar.search((1, 1), (31,39))
    path = astar.search((1, 1), (31,39), True)

    length = len(path) - 1
    print 'part1 : %d' % (length)


if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
