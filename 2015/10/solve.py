#!/usr/bin/env python

ITERATIONS = 40
def main(lines):
    for sequence in lines:
        print 'old : ' + sequence
        for i in range(1, ITERATIONS+1):
            sequence = new_sequence(sequence)

        part1 = len(sequence)
        part2 = ''

        print 'part 1 : %s' % (part1)
        print 'part 2 : %s' % (part2)

def new_sequence(sequence):
    digit = sequence[0]
    count = 0
    builder = []
    for i in sequence:
        if i != digit:
            builder.append(str(count) + digit)
            digit = i
            count = 0
        count += 1

    builder.append(str(count) + digit)
    return ''.join(builder)







if __name__ == '__main__':
    test_input = [
        # '1',
        # '11',
        # '21',
        # '1211',
        # '111221'

    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
