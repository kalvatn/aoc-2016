#!/usr/bin/env python
import unittest

class Test(unittest.TestCase):
    def test_part_one(self):

        cases = [
                { 'input' : 'ADVENT',            'expect' : 'ADVENT',              'expect_length' : 6 },
                { 'input' : 'A(1x5)BC',          'expect' : 'ABBBBBC',             'expect_length' : 7 },
                { 'input' : '(3x3)XYZ',          'expect' : 'XYZXYZXYZ',           'expect_length' : 9 },
                { 'input' : 'A(2x2)BCD(2x2)EFG', 'expect' : 'ABCBCDEFEFG',         'expect_length' : 11 },
                { 'input' : '(6x1)(1x3)A',       'expect' : '(1x3)A',              'expect_length' : 6 },
                { 'input' : 'A(2x2)BCD(2x2)EFG', 'expect' : 'ABCBCDEFEFG',         'expect_length' : 11 },
                { 'input' : 'X(8x2)(3x3)ABCY',   'expect' : 'X(3x3)ABC(3x3)ABCY',  'expect_length' : 18 },
            ]
        for case in cases:
            decompressed = decompress_one(case['input'])
            self.assertEqual(decompressed, case['expect'])
            self.assertEqual(len(decompressed), case['expect_length'])

LB = '('
RB = ')'
def main(lines):
    total_length = 0
    for line in lines:
        decompressed_one = decompress_one(line)
        total_length += len(decompressed_one)


    part1 = total_length
    part2 = ''

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def decompress_one(line):
    i = 0
    decompressed = ''
    while i < len(line):
        if line[i] == LB:
            i += 1
            close = line.find(RB, i)
            repeat_range, repeat = [int (c) for c in line[i:close].split('x')]
            i += close - i + 1
            repeat_text = line[i:i+repeat_range]
            decompressed += repeat_text * repeat
            i += repeat_range
        else:
            decompressed += line[i]
            i += 1
    return decompressed


if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
