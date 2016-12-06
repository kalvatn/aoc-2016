#!/usr/bin/env python

LEFT_PAREN  = '('
RIGHT_PAREN = ')'

def main(lines):
    parens = lines[0]
    floor = 0
    position = 0
    basement_found = False
    for paren in parens:
        updown = 1 if paren == LEFT_PAREN else -1

        floor += updown
        if not basement_found:
            position += 1
            if floor == -1:
                basement_found = True

    print 'part 1 : %d' % (floor)
    print 'part 2 : %d' % (position)


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
