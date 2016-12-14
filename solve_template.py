#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

def main(lines):
    part1 = None
    part2 = None

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
