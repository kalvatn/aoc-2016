#!/usr/bin/env python

import unittest
from string import ascii_lowercase as alphabet
from collections import deque

def reverse(s):
    return s[::-1]

def reverse_range(s, start, end):
    return s[:start] + reverse(s[start:end+1]) + s[end+1:]

def replace(s, to_replace, replacement):
    return s.replace(to_replace, replacement)

def replace_char_at_index(s, index, replacement):
    return s[:index] + replacement + s[index+1:]

def replace_in_range(s, start, end, to_replace, replacement):
    return s[:start] + replace(s[start:end+1], to_replace, replacement) + s[end+1:]

def replace_all_in_range(s, start, end, replacement):
    if end > len(s):
        end = len(s)
    return s[:start] + replacement * (end-start) + s[end+1:]

def rotate(s, by):
    rotated = deque(s)
    rotated.rotate(by)
    return ''.join(rotated)

def rotate_by_char_pos(s, char):
    return rotate(s, s.index(char))

def rotate_by_char_pos_day21(s, char):
    index = s.index(char)
    num_rotations = 1 + index
    if index >= 4:
        num_rotations += 1
    return rotate(s, num_rotations)

def swap_index(s, index1, index2):
    low = index1 if index1 < index2 else index2
    high = index2 if index2 > index1 else index1
    return s[:low] + s[high] + s[low+1:high] + s[low] + s[high+1:]

def swap_char(s, char1, char2):
    return swap_index(s, s.index(char1), s.index(char2))

def move_char(s, from_index, to_index):
    if to_index > from_index:
        return s[:from_index] + s[from_index+1:to_index+1] + s[from_index] + s[to_index+1:]
    else:
        return s[:to_index] + s[from_index] + s[to_index:from_index] + s[from_index+1:]

class Test(unittest.TestCase):
    def test_reverse(self):
        self.assertEquals(reverse('abcde'), 'edcba')

    def test_reverse_range(self):
        self.assertEquals(reverse_range('edcba', 0, 4), 'abcde')
        self.assertEquals(reverse_range('abcde', 2, 3), 'abdce')

    def test_replace_char(self):
        self.assertEquals(replace('aaaaa', 'a', 'X'), 'XXXXX')
        self.assertEquals(replace('abcde', 'a', 'X'), 'Xbcde')
        self.assertEquals(replace('aaabbaaa', 'a', 'X'), 'XXXbbXXX')

        self.assertEquals(replace('abcde', 'abcde', 'X'), 'X')
        self.assertEquals(replace('abcde', 'ab', 'X'), 'Xcde')

    def test_replace_char_at_index(self):
        self.assertEquals(replace_char_at_index('abcde', 2, 'X'), 'abXde')
        self.assertEquals(replace_char_at_index('abcde', 0, 'X'), 'Xbcde')
        self.assertEquals(replace_char_at_index('abcdX', 4, 'X'), 'abcdX')
        self.assertEquals(replace_char_at_index('a', 0, 'X'), 'X')

    def test_replace_in_range(self):
        self.assertEquals(replace_in_range('aaaaa', 0, 2, 'a', 'X'), 'XXXaa')
        self.assertEquals(replace_in_range('aaaaabbbcccdeeeaaaa', 0, 15, 'a', 'X'), 'XXXXXbbbcccdeeeXaaa')

    def test_replace_all_in_range(self):
        self.assertEquals(replace_all_in_range('aaaaabbbbbcccccddddd', 0, 15, 'X'), 'XXXXXXXXXXXXXXXdddd')
        self.assertEquals(replace_all_in_range('aaaaa', 0, 15, 'X'), 'XXXXX')

    def test_rotate(self):
        self.assertEquals(rotate('abcde', 1), 'eabcd')
        self.assertEquals(rotate('abcde', 5), 'abcde')
        self.assertEquals(rotate('abcde', -1), 'bcdea')

    def test_rotate_by_char_pos(self):
        self.assertEquals(rotate_by_char_pos('abdec', 'b'), 'cabde')

    def test_rotate_by_char_pos_day21(self):
        self.assertEquals(rotate_by_char_pos_day21('abdec', 'b'), 'ecabd')
        self.assertEquals(rotate_by_char_pos_day21('ecabd', 'd'), 'decab')

    def test_swap(self):
        self.assertEquals(swap_index('abcde', 4, 0), 'ebcda')
        self.assertEquals(swap_char('ebcda', 'b', 'd'), 'edcba')

    def test_move_char(self):
        self.assertEquals(move_char('bcdea', 1, 4), 'bdeac')
        self.assertEquals(move_char('bdeac', 3, 0), 'abdec')

    def test_all(self):
        s = 'abcde'
        s = swap_index(s, 4, 0)
        s = swap_char(s, 'd', 'b')
        s = reverse_range(s, 0, 4)
        s = rotate(s, -1)
        s = move_char(s, 1, 4)
        s = move_char(s, 3, 0)
        s = rotate_by_char_pos_day21(s, 'b')
        s = rotate_by_char_pos_day21(s, 'd')
        self.assertEquals(s, 'decab')



if __name__ == '__main__':
    unittest.main()

