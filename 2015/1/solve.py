#!/usr/bin/env python

LEFT_PAREN  = '('
RIGHT_PAREN = ')'

def main(lines):
    parens = lines[0]
    floor = 0
    for paren in parens:
        if paren == LEFT_PAREN:
            floor += 1
        elif paren == RIGHT_PAREN:
            floor -= 1
    print floor


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
