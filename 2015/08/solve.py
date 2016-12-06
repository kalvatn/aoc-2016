#!/usr/bin/env python


def main(lines):
    sum_code_chars = 0
    sum_string_chars = 0

    for line in lines:
        num_code_chars = len(line)
        num_string_chars = count_string_chars(line)

        # print "'%s' code : %d, string : %d" % (line, num_code_chars, num_string_chars)

        sum_code_chars += num_code_chars
        sum_string_chars += num_string_chars

    part1 = sum_code_chars - sum_string_chars
    part2 = ''

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def count_string_chars(line):
    result = line
    result = result.replace(' ', '')
    result = result.decode('string-escape')
    result = result[result.find('"')+1:result.rfind('"')]

    return len(result)

if __name__ == '__main__':
    test_input = [
        # '""',
        # '"abc"',
        # '"aaa\\"aaa"',
        # '"\\x27"'
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
