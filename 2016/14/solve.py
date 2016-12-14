#!/usr/bin/env python

import unittest
import hashlib
from string import ascii_lowercase as letters

class Test(unittest.TestCase):
    def test_part_one_examples(self):
        pass

    def test_part_two_examples(self):
        pass



def main(lines):
    numbers = ''.join([str(i) for i in range(0, 10)])
    triplets = [ a*3 for a in numbers + letters ]
    quintuplets = [ a*5 for a in numbers + letters ]
    salt = lines[0]
    # salt = 'abc'
    candidates = {}

    triplet_hashes = {}
    quintuplet_hashes = {}
    found_key_indexes = set()
    i = 0
    while len(found_key_indexes) < 64:
        tohash = '%s%d' % (salt, i)
        hashed = hashlib.md5(tohash).hexdigest()
        for triplet in triplets:
            if triplet in hashed:
                triplet_hashes[i] = (hashed, triplet)
        for quintuplet in quintuplets:
            if quintuplet in hashed:
                quintuplet_hashes[i] = (hashed, quintuplet)
        # print '%d, tohash : %s, hash : %s' % (i, tohash, hashed)
        i += 1
        if i % 10000 == 0:
            for tk, tv in triplet_hashes.items():
                if tk not in found_key_indexes:
                    for qk, qv in quintuplet_hashes.items():
                        if qv[1].startswith(tv) and qk > tk and (qk - tk <= 1000):
                            if tk not in found_key_indexes:
                                found_key_indexes.add((tk, qk))
                            # print '%d -> %d (%s -> %s)' % (tk, qk, triplet_hashes[tk], quintuplet_hashes[qk])

    print salt
    # found_key_indexes = sorted(found_key_indexes)
    found_key_indexes = sorted(found_key_indexes)
    print found_key_indexes[63]
    i = 0
    for tk, qk in found_key_indexes:
        triplet = triplet_hashes[tk]
        quintuplet = quintuplet_hashes[qk]

        print '%d -> %d (%d) (%s -> %s)' % (tk, qk, qk - tk, triplet, quintuplet)





    part1 = None
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
