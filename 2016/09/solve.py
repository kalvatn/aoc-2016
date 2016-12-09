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
    def test_part_two(self):
        cases = {
            { 'input' : '(3x3)XYZ',                                                 'expect_length' : 9 },
            { 'input' : 'X(8x2)(3x3)ABCY',                                          'expect_length' : 20 },
            { 'input' : '(27x12)(20x12)(13x14)(7x10)(1x12)A',                       'expect_length' : 241920 },
            { 'input' : '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 'expect_length' : 445 },
        }
        for case in cases:
            self.assertEqual(decompress_two(case['input']), case['expect_length'])

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

def decompress_two(line):
    i = 0
    length = 0
    decompressed = ''
    while i < len(line):
        if line[i] == LB:
            i += 1
            close = line.find(RB, i)
            repeat_range, repeat = [int (c) for c in line[i:close].split('x')]
            i += close - i + 1
            repeat_text = line[i:i+repeat_range]
            if repeat_text.find(LB):
                length += decompress_two(repeat_text)

            decompressed += repeat_text * repeat
            i += repeat_range
        else:
            decompressed += line[i]
            i += 1
    return len(decompressed)


if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
