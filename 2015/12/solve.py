#!/usr/bin/env python

import unittest
import json

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

def get_number_sum(data, ignore=None):
    number_sum = 0
    try:
        number_sum += int(data)
    except :
        if isinstance(data, list):
            for item in data:
                number_sum += get_number_sum(item, ignore=ignore)
        elif isinstance(data, dict):
            if ignore and ignore in data.values():
                # print 'ignoring red data %s' % data
                pass
            else:
                number_sum += get_number_sum(data.values(), ignore=ignore)
        else:
            # print 'unknown data %s' % data
            pass
    return number_sum

def main(lines):
    json_data = json.loads(''.join(lines))

    part1 = get_number_sum(json_data)

    part2 = get_number_sum(json_data, 'red')

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
