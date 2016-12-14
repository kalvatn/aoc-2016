#!/usr/bin/env python

import unittest
import json

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass

def get_number_sum(data):
    number_sum = 0
    try:
        number_sum += int(data)
    except :
        if isinstance(data, list):
            for item in data:
                # items.append(get_number_sum(item))
                number_sum += get_number_sum(item)
        elif isinstance(data, dict):
            for k,v in data.items():
                number_sum += get_number_sum(data[k])
        else:
            # print 'unknown data %s' % data
            pass
    return number_sum

def main(lines):
    json_data = json.loads(''.join(lines))

    part1 = get_number_sum(json_data)

    part2 = None

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
