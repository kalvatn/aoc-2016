#!/usr/bin/env python

from stdlib import aoc

class Day8(aoc.Day):
    def __init__(self):
        super(Day8, self).__init__(__file__)

    def run(self):
        lines = self.read_input()
        sum_code_chars = 0
        sum_string_chars = 0

        for line in lines:
            num_code_chars = len(line)
            num_string_chars = self.count_string_chars(line)

            # print "'%s' code : %d, string : %d" % (line, num_code_chars, num_string_chars)

            sum_code_chars += num_code_chars
            sum_string_chars += num_string_chars

        part1 = sum_code_chars - sum_string_chars
        part2 = ''

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

    def count_string_chars(self, line):
        result = line
        result = result.replace(' ', '')
        result = result.decode('string-escape')
        result = result[result.find('"')+1:result.rfind('"')]

        return len(result)

if __name__ == '__main__':
    Day8().run()
