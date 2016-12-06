#!/usr/bin/env python

WIRES = {
}

AND     = 'AND'
OR      = 'OR'
NOT     = 'NOT'
LSHIFT  = 'LSHIFT'
RSHIFT  = 'RSHIFT'

MAX = 65535

def main(lines):
    lines = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]

    retry_lines = []
    for line in lines:
        print line
        retry = process_line(line)
        if retry:
            retry_lines.append(retry)

    for line in retry_lines:
        print line
        process_line(line)

    for k, v in WIRES.items():
        if int(v) < 0:
            WIRES[k] = (65535 + int(WIRES[k])) + 1
        print "%s -> %d" % (k, WIRES[k])

    try:
        print WIRES['a']
    except KeyError:
        pass

def process_line(line):
    inputs, output = line.split(' -> ')
    # print "input : '%s', output : '%s'" % (inputs, output)
    if output not in WIRES:
        WIRES[output] = 0

    if output == 'a':
        print WIRES['a']

    try:
        op = None
        for operation in [AND, OR, NOT, LSHIFT, RSHIFT]:
            if operation in inputs:
                op = operation
                break



        if op:
            if op == AND:
                left, right = get_left_right(inputs.split(AND))
                value = left & right
            elif op == OR:
                left, right = get_left_right(inputs.split(OR))
                value = left | right
            elif op == NOT:
                right = inputs.split(NOT)[1]
                right = int(WIRES[right.strip()])
                value = ~right
            elif op == LSHIFT:
                left, places = inputs.split(LSHIFT)
                left = int(WIRES[left.strip()])
                places = int(places)
                value = left << places
            elif op == RSHIFT:
                left, places = inputs.split(RSHIFT)
                left = int(WIRES[left.strip()])
                places = int(places)
                value = left >> places

        else:
            try:
                value = int(inputs)
            except ValueError:
                value = int(WIRES[inputs])

        value = MAX + value + 1 if value < 0 else value
        WIRES[output] = value

    except KeyError:
        return line

    return None

def get_left_right(inputs):
    return [ int(WIRES[x.strip()]) for x in inputs ]





if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
