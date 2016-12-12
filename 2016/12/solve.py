#!/usr/bin/env python

import unittest

class Machine(object):
    def __init__(self, instructions=[]):
        self._registers = {
            'a' : 0,
            'b' : 0,
            'c' : 0,
            'd' : 0
        }
        self._instructions = instructions
        self._instruction_index = 0

    @property
    def registers(self):
        return self._registers

    @property
    def instructions(self):
        return self._instructions

    @property
    def cursor(self):
        return self._instruction_index

    def set_register(self, register, value):
        self._registers[register] = value

    def cpy(self, register, value):
        self._registers[register] = value

    def inc(self, register):
        self._registers[register] += 1

    def dec(self, register):
        self._registers[register] -= 1

    def jnz(self, register, jump):
        # print 'before jnz(%s, %d), cursor : %d' % (register, jump, self.cursor)
        # print self.registers
        register_value = 0
        try:
            register_value = int(register)
        except ValueError:
            register_value = self._registers[register]

        if register_value != 0:
            next_index = self.cursor + jump - 1
            self._instruction_index = next_index if next_index <= len(self.instructions) and next_index >= 0 else self.cursor
        # print 'after jnz(%s, %d), cursor : %d' % (register, jump, self.cursor)

    def run_instruction(self):
        instruction = self.instructions[self.cursor]
        parts = instruction.split()
        # print "instruction '%s', parts : %s, registers : %s" % (instruction, parts, self.registers)
        if parts[0] == 'cpy':
            try:
                self.cpy(parts[2], int(parts[1]))
            except ValueError:
                self.cpy(parts[2], self._registers[parts[1]])
        elif parts[0] == 'inc':
            self.inc(parts[1])
        elif parts[0] == 'dec':
            self.dec(parts[1])
        elif parts[0] == 'jnz':
            self.jnz(parts[1], int(parts[2]))
        else:
            raise ValueError("invalid instruction '%s'" % (instruction))

    def step(self):
        self.run_instruction()
        self._instruction_index += 1

    def process_instructions(self):
        while self.cursor >= 0 and self.cursor < len(self.instructions):
            self.step()

class Test(unittest.TestCase):

    def setUp(self):
        self.machine = Machine()

    def test_inc(self):
        self.machine.inc('a')
        self.machine.inc('a')
        self.assertEquals(self.machine.registers['a'], 2)


    def test_dec(self):
        self.machine.dec('a')
        self.machine.dec('a')
        self.assertEquals(self.machine.registers['a'], -2)


    def test_cpy(self):
        self.machine.cpy('a', 41)
        self.assertEquals(self.machine.registers['a'], 41)

        self.machine.cpy('a', 1001)
        self.assertEquals(self.machine.registers['a'], 1001)

    def test_cursor(self):
        instructions = [
            'cpy -2 a',
            'inc a',
            'cpy 2 b',
            'cpy 3 c',
            'cpy 4 b',
            'jnz a -4'
        ]
        self.machine = Machine(instructions)
        self.machine.process_instructions()
        # self.assertEquals(self.machine.cursor, 0)
        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 1)
        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 2)
        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 3)
        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 4)

        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 5)

        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 1)

        # self.machine.step()
        # self.assertEquals(self.machine.cursor, 2)

    def test_part_one_example(self):
        """ jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.  """
        instructions = [
                'cpy 41 a',
                'inc a',
                'inc a',
                'dec a',
                'jnz a 2',
                'dec a',
        ]
        self.machine = Machine(instructions)
        self.machine.process_instructions()
        self.assertEquals(self.machine.registers['a'], 42)

    # @unittest.skip("skip")
    def test_part_one(self):
        # import time
        instructions = [ line.strip() for line in open('input').readlines() ]
        self.machine = Machine(instructions)
        self.machine.process_instructions()
        print self.machine.registers['a']
        # while self.machine.cursor >= 0 and self.machine.cursor <= len(instructions):

        #     self.machine.step()
        #     time.sleep(0.5)
        #     # print self.machine.registers


    def test_part_two(self):
        instructions = [ line.strip() for line in open('input').readlines() ]
        self.machine = Machine(instructions)
        self.machine.set_register('c', 1)
        self.machine.process_instructions()
        print self.machine.registers['a']

def main(lines):
    print lines

    puzzle_input = parse_lines(lines)

    part1 = part_one(puzzle_input)
    part2 = part_two(puzzle_input)

    print 'part 1 : %s' % (part1)
    print 'part 2 : %s' % (part2)

def init(register, registers):
    if register not in registers:
        registers[register] = 0


def part_one(puzzle_input):
    return ''

def part_two(puzzle_input):
    return ''


if __name__ == '__main__':
    unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
