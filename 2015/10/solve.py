#!/usr/bin/env python

def main(lines):
    sequence = lines[0]


    part1 = len(sequence)
    part2 = ''

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)


if __name__ == '__main__':
    test_input = [
        # 'test',
        # 'strings',
        # 'here'
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
