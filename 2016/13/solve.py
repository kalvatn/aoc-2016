#!/usr/bin/env python

import unittest
import time

WALL='#'
OPEN='.'

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
        return 0 if self.value == OPEN else 1

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
        return x >= 0 and x < len(self.table) and y >= 0 and y < len(self.table) and self.nodes[x][y].value != WALL

    def get_neighbours(self, node):
        x, y = node.x, node.y
        left = (x-1, y)
        right = (x+1, y)
        up = (x, y-1)
        down = (x, y+1)
        return [ self.nodes[point[0]][point[1]] for point in [ left, right, up, down ] if self.is_valid_point(point) ]

    def get_manhattan_distance(self, node, goal):
        return abs(node.x - goal.x) + abs(node.y - node.x)

    def search(self, start_point, goal_point, step=False):
        start = self.nodes[start_point[0]][start_point[1]]
        goal = self.nodes[goal_point[1]][goal_point[0]]
        print 'start : %s' % start
        print 'goal : %s' % goal
        current = start
        self.open.add(current)
        followed_path = []
        while self.open:
            current = min(self.open, key=lambda node: node.get_f_score())
            followed_path.append((current.x, current.y))
            if step:
                print_map(self.table, followed_path)
                time.sleep(1)
            if current == goal:
                path = []
                while current.parent:
                    path.append((current.x, current.y))
                    current = current.parent
                path.append((current.x, current.y))
                return path[::-1]
            self.open.remove(current)
            self.closed.add(current)
            for node in self.get_neighbours(current):
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
        raise ValueError('no valid path found')

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass


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
    header += ''.join([ '%d' % x for x in range(0, len(table))])
    print header
    for x in range(0, len(table)):
        row = '%d ' % (x)
        for y in range(0, len(table[x])):
            if (x, y) in path:
                indicator = 'P'
                if (x, y) == path[0]:
                    indicator = 'S'

                if (x, y) == path[-1]:
                    indicator = 'G'
                row += '%s' % (indicator)
            else:
                row += '%s' % (table[x][y])
        print row



def main(lines):
    width = 10
    height = 10
    magic_number = 10
    # magic_number = int(lines[0])
    table = [[get_map_value(x, y, magic_number) for x in range(0,width)] for y in range(0, height)]
    print_map(table)

    astar = AStar(table)
    # path = astar.search((1, 1), (7,4))
    path = astar.search((1, 1), (7,4), True)
    # print_map(table, path)
    print 'part1 : %d' % (len(path) - 1)


if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
