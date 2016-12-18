#!/usr/bin/env python

import hashlib
from stdlib import aoc

class Day4(aoc.Day):
    def __init__(self):
        super(Day4, self).__init__(__file__)

    def run(self):
        secret = self.read_input()[0]
        index = 0
        part1 = False
        part2 = False
        while not part1 or not part2:
            digest = hashlib.md5(secret + str(index)).hexdigest()
            if not part1 and digest.startswith('00000'):
                part1 = True
                self.log.info('part 1 : %d' % (index))

            if not part2 and digest.startswith('000000'):
                part2 = True
                self.log.info('part 2 : %d' % (index))
            index += 1

if __name__ == '__main__':
    Day4().run()
