#!/usr/bin/env python

WIRES = {}
WIRE_RESULTS = {}

AND     = 'AND'
OR      = 'OR'
NOT     = 'NOT'
LSHIFT  = 'LSHIFT'
RSHIFT  = 'RSHIFT'

MAX = 65535

def main(lines):
    # lines = [
    #     '123 -> x',
    #     '456 -> y',
    #     'x AND y -> d',
    #     'x OR y -> e',
    #     'x LSHIFT 2 -> f',
    #     'y RSHIFT 2 -> g',
    #     'NOT x -> h',
    #     'NOT y -> i',
    # ]

    for line in lines:
        print line
        inputs, output = line.split(' -> ')
        WIRES[output.strip()] = inputs.strip().split(' ')

    print WIRES
    print get_wire('a')

    # print WIRE_RESULTS


def get_wire(key):
    if key.isdigit():
        return int(key)
    if key not in WIRE_RESULTS:
        operation = WIRES[key]
        if len(operation) == 1:
            result = get_wire(operation[0])
        else:
            oper = operation[-2]
            if oper == AND:
                result = get_wire(operation[0]) & get_wire(operation[2])
            elif oper == OR:
                result = get_wire(operation[0]) | get_wire(operation[2])
            elif oper == NOT:
                result = ~get_wire(operation[1]) & 0xffff
            elif oper == LSHIFT:
                result = get_wire(operation[0]) << get_wire(operation[2])
            elif oper == RSHIFT:
                result = get_wire(operation[0]) >> get_wire(operation[2])
        WIRE_RESULTS[key] = result

    return WIRE_RESULTS[key]


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
