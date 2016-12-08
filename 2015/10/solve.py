#!/usr/bin/env python

def main(lines):
    for sequence in lines:
        original = sequence
        for i in range(0, 40):
            sequence = new_sequence(sequence)

        print 'part 1 : %s' % (len(sequence))
        sequence = original
        for i in range(0, 50):
            sequence = new_sequence(sequence)

        print 'part 2 : %s' % (len(sequence))

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
