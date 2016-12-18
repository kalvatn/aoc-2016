#!/usr/bin/env python

from stdlib import aoc

WIRES = {}
WIRE_RESULTS = {}

AND     = 'AND'
OR      = 'OR'
NOT     = 'NOT'
LSHIFT  = 'LSHIFT'
RSHIFT  = 'RSHIFT'

MAX = 65535

class Day7(aoc.Day):
    def __init__(self):
        super(Day7, self).__init__(__file__)

    def run(self):
        lines = self.read_input()
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
            inputs, output = line.split(' -> ')
            WIRES[output.strip()] = inputs.strip().split(' ')

        part1 = self.get_wire('a')
        WIRE_RESULTS.clear()

        WIRES['b'] = [ str(part1) ]
        part2 = self.get_wire('a')

        self.log.info('part 1 : %d' % part1)
        self.log.info('part 2 : %d' % part2)

    def reset_wires(self, lines):
        WIRES.clear()
        WIRE_RESULTS.clear()

    def get_wire(self, key):
        if key.isdigit():
            return int(key)
        if key not in WIRE_RESULTS:
            operation = WIRES[key]
            if len(operation) == 1:
                result = self.get_wire(operation[0])
            else:
                oper = operation[-2]
                if oper == AND:
                    result = self.get_wire(operation[0]) & self.get_wire(operation[2])
                elif oper == OR:
                    result = self.get_wire(operation[0]) | self.get_wire(operation[2])
                elif oper == NOT:
                    result = ~self.get_wire(operation[1]) & 0xffff
                elif oper == LSHIFT:
                    result = self.get_wire(operation[0]) << self.get_wire(operation[2])
                elif oper == RSHIFT:
                    result = self.get_wire(operation[0]) >> self.get_wire(operation[2])
            WIRE_RESULTS[key] = result

        return WIRE_RESULTS[key]


if __name__ == '__main__':
    Day7().run()
