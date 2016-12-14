#!/usr/bin/env python

import unittest

from string import ascii_lowercase as letters

STRAIGHTS = [ letters[i:i+3] for i in range(0, len(letters) - 2) ]
PAIRS = [ letter * 2 for letter in letters ]
AMBIGUOUS = [ l for l in 'iol' ]

class Test(unittest.TestCase):

    def test_has_straight(self):
        self.assertTrue(has_straight('abcdef'))
        self.assertTrue(has_straight('abc'))
        self.assertTrue(has_straight('def'))

        self.assertTrue(has_straight('abdcde'))

        self.assertFalse(has_straight('abdc'))
        self.assertFalse(has_straight('abdcxzyacd'))

    def test_has_two_pair(self):
        self.assertTrue(has_two_pair('aabb'))
        self.assertTrue(has_two_pair('aacddefg'))
        self.assertFalse(has_two_pair('aaaa'))
        self.assertFalse(has_two_pair('aaxyzaia'))

    def has_ambiguous(self):
        self.assertTrue(has_ambiguous('iol'))
        self.assertTrue(has_ambiguous('indigol'))
        self.assertFalse(has_ambiguous('abcdefghjkmnpqrstuvxyz'))

    def test_part_one_examples(self):
        self.assertFalse(is_valid('hijklmmn'))
        self.assertFalse(is_valid('abbceffg'))
        self.assertFalse(is_valid('abbcegjk'))
        self.assertFalse(is_valid('ghijklmn'))

        self.assertTrue(is_valid('abcdffaa'))
        self.assertTrue(is_valid('ghjaabcc'))

        self.assertTrue(is_valid('abcddmxx'))

    def test_get_letter_index(self):
        self.assertEquals(get_letter_index('a'), 0)
        self.assertEquals(get_letter_index('b'), 1)

        self.assertEquals(get_letter_index('z'), 25)

    def test_increment(self):
        self.assertEquals(get_new_letter_index('a'), 1)
        self.assertEquals(get_new_letter_index('b'), 2)
        self.assertEquals(get_new_letter_index('z'), 0)
        self.assertEquals(increment('a'), 'b')
        self.assertEquals(increment('b'), 'c')
        self.assertEquals(increment('z'), 'a')

        self.assertEquals(increment('abc'), 'bcd')
        self.assertEquals(increment('abz'), 'bcd')

    @unittest.skip('skip find next')
    def test_find_next(self):
        self.assertEquals(find_next('abcdefgh'), 'abcdffaa')
        self.assertEquals(find_next('ghijklmn'), 'ghjaabcc')

        pass

    def test_part_two_examples(self):
        pass


def has_straight(password):
    for i in range(0, len(password) - 2):
        if password[i:i+3] in STRAIGHTS:
            return True
    return False

def has_two_pair(password):
    found_pairs = set()
    for i in range(0, len(password) - 1):
        pair = password[i:i+2]
        if pair in PAIRS and pair not in found_pairs:
            found_pairs.add(pair)
            if len(found_pairs) >= 2:
                return True
    return False

def has_ambiguous(password):
    for a in AMBIGUOUS:
        if a in password:
            return True
    return False

def is_valid(password):
    return has_straight(password) and has_two_pair(password) and not has_ambiguous(password)

def get_letter_index(letter):
    return letters.index(letter)

def get_new_letter_index(letter):
    index = get_letter_index(letter)
    index = 0 if index + 1 >= len(letters) else index + 1
    return index

def increment_letter(letter):
    return letters[get_new_letter_index(letter)]

def increment(password):
    print password
    new_password = ''
    found_wrap = False
    for letter in reversed(password):
        new_letter = increment_letter(letter)
        new_password += new_letter

        if found_wrap:
            break
        if new_letter == 'a':
            found_wrap = True
    return ''.join(reversed(new_password))


def find_next(password):
    return password

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
