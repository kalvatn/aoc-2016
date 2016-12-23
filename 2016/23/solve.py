from stdlib import aoc

import time

class Machine(object):
    def __init__(self, instructions=[], log=None):
        self._registers = {
            'a' : 0,
            'b' : 0,
            'c' : 0,
            'd' : 0
        }
        self._instructions = instructions
        self._instruction_index = 0
        self.log = log

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
        jump_value = 0
        try:
            register_value = int(register)
        except ValueError:
            register_value = int(self._registers[register])

        try:
            jump_value = int(jump)
        except ValueError:
            jump_value = int(self._registers[jump])


        if register_value != 0:
            next_index = self.cursor + jump_value - 1
            self._instruction_index = next_index if next_index <= len(self.instructions) and next_index >= 0 else self.cursor
        # print 'after jnz(%s, %d), cursor : %d' % (register, jump, self.cursor)

    def tgl(self, register):
        register_value = 0

        try:
            register_value = int(register)
        except ValueError:
            register_value = self._registers[register]

        instruction_index = self.cursor + register_value
        if 0 <= instruction_index < len(self._instructions):
            self.convert_instruction(instruction_index)

    def convert_instruction(self, instruction_index):
        original_instruction = self._instructions[instruction_index]
        new_instruction = ''
        parts = original_instruction.split()
        cmd, args = parts[0], parts[1:]
        if len(args) == 1:
            if cmd == 'inc':
                new_instruction = 'dec ' + ' '.join(args)
            else:
                new_instruction = 'inc ' + ' '.join(args)
        else:
            if cmd == 'jnz':
                new_instruction = 'cpy ' + ' '.join(args)
            else:
                new_instruction = 'jnz ' + ' '.join(args)

        self.log.debug('instructions[%d] %s toggled -> %s' % (instruction_index, original_instruction, new_instruction))

        self._instructions[instruction_index] = new_instruction

    def run_instruction(self):
        instruction = self.instructions[self.cursor]
        parts = instruction.split()
        cmd, args = parts[0], parts[1:]
        # self.log.debug("instruction[%2d] '%10s', parts : %s, registers : %s" % (self.cursor, instruction, parts, self.registers))
        if cmd == 'cpy':
            try:
                self.cpy(args[1], int(args[0]))
            except ValueError:
                self.cpy(args[1], self._registers[args[0]])
        elif cmd == 'inc':
            self.inc(args[0])
        elif cmd == 'dec':
            self.dec(args[0])
        elif cmd == 'jnz':
            self.jnz(args[0], args[1])
        elif cmd == 'tgl':
            self.tgl(args[0])
        else:
            raise ValueError("invalid instruction '%s'" % (instruction))

        self.log.debug("instruction[%2d] '%8s' : registers : %s" % (self.cursor, instruction, self.registers))

    def step(self):
        self.run_instruction()
        self._instruction_index += 1

    def process_instructions(self, visualize=False):
        while self.cursor >= 0 and self.cursor < len(self.instructions):
            self.step()
            if visualize:
                time.sleep(0.5)

class Day23(aoc.Day):
    def __init__(self):
        super(Day23, self).__init__(__file__)

    def part_one(self):
        instructions = self.read_input()
        # instructions = self.read_input(input_file='example_input')
        self.machine = Machine(instructions, log=self.log)
        self.machine._registers['a'] = 7
        self.machine.process_instructions(self.visualize)
        return self.machine.registers['a']

    def part_two(self):
        instructions = self.read_input()
        # instructions = self.read_input(input_file='example_input')
        self.machine = Machine(instructions, log=self.log)
        self.machine._registers['a'] = 12
        self.machine.process_instructions(self.visualize)
        return self.machine.registers['a']


    def run(self):
        self.log.info('part 1 : %d' % (self.part_one()))
        time.sleep(5)
        self.log.info('part 2 : %d' % (self.part_two()))

if __name__ == '__main__':
    Day23().run()

