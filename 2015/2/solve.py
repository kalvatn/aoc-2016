#!/usr/bin/env python

def main(lines):
    print lines


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
