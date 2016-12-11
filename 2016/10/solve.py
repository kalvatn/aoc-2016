#!/usr/bin/env python

import unittest
from collections import deque


class Bot(object):
    def __init__(self, name):
        self.name = name
        self.values = []

    def low(self):
        if self.values:
            return self.values.pop(self.values.index(min(self.values)))
        return None

    def high(self):
        if self.values:
            return self.values.pop(self.values.index(max(self.values)))
        return None

    def receive_value(self, value):
        self.values.append(value)

    def __str__(self):
        return '%s : %s' % (self.name, self.values)

    def __repr__(self):
        return '%s' % (self.values)

class OutputBin(object):
    def __init__(self, name):
        self.name = name
        self._values = []

    @property
    def values(self):
        return self._values

    def receive_value(self, value):
        self._values.append(value)

    def __str__(self):
        return '%s : %s' % (self.name, self.values)

    def __repr__(self):
        return '%s' % (self.values)


class InitialValueCommand(object):
    def __init__(self, bot, value):
        self.bot = bot
        self.value = value

    def __str__(self):
        return '%s initial %d' % (self.bot, self.value)

class GiveValueCommand(object):
    def __init__(self, giver, low_receiver, high_receiver):
        self.giver = giver
        self.low_receiver = low_receiver
        self.high_receiver = high_receiver

    def __str__(self):
        return '%s gives low -> %s, high -> %s' % (self.giver, self.low_receiver, self.high_receiver)

    def __repr__(self):
        return str(self)


class Test(unittest.TestCase):

    def test_parse_input(self):
        command = parse_line('value 5 goes to bot 2')
        self.assertTrue(isinstance(command, InitialValueCommand))
        self.assertEquals(command.bot, 'bot 2')
        self.assertEquals(command.value, 5)

        command = parse_line('bot 2 gives low to bot 1 and high to bot 0')
        self.assertTrue(isinstance(command, GiveValueCommand))
        self.assertEquals(command.giver, 'bot 2')
        self.assertEquals(command.low_receiver, 'bot 1')
        self.assertEquals(command.high_receiver, 'bot 0')

        command = parse_line('bot 1 gives low to output 1 and high to bot 0')
        self.assertTrue(isinstance(command, GiveValueCommand))
        self.assertEquals(command.giver, 'bot 1')
        self.assertEquals(command.low_receiver, 'output 1')
        self.assertEquals(command.high_receiver, 'bot 0')

    def test_apply_command(self):
        bots = {}
        outputs = {}
        apply_command(InitialValueCommand('bot 2', 5), bots, outputs)
        apply_command(InitialValueCommand('bot 1', 3), bots, outputs)
        apply_command(InitialValueCommand('bot 2', 2), bots, outputs)
        self.assertEquals(bots['bot 2'].values, [5, 2])
        self.assertEquals(bots['bot 1'].values, [3])


        apply_command(GiveValueCommand('bot 2', 'bot 1', 'bot 0'), bots, outputs)
        self.assertEquals(bots['bot 1'].values, [3, 2])
        self.assertEquals(bots['bot 0'].values, [5])

        # print 'bots : %s' % bots
        # print 'outputs : %s' % outputs




    def test_bot(self):
        bot = Bot('bot 1')
        self.assertEquals(bot.high(), None)
        self.assertEquals(bot.low(), None)
        bot.receive_value(10)
        bot.receive_value(5)
        self.assertEquals(bot.high(), 10)
        self.assertEquals(bot.low(), 5)

    def test_output_bin(self):
        output = OutputBin('output 0')
        output.receive_value(10)
        output.receive_value(1)
        self.assertEquals(output.values, [ 10, 1 ])


def main(lines):
    # print lines

    commands = parse_lines(lines)

    bots, outputs = part_one(commands)
    part2 = part_two(outputs)

    print 'part 2 : %s' % (part2)

def parse_lines(lines):
    return [ parse_line(line) for line in lines ]

def parse_line(line):
    if line.startswith('value '):
        value, bot = line.split(' goes to ')
        return InitialValueCommand(bot, int(value.split('value')[1]))

    if line.startswith('bot '):
        giver, rest = line.split(' gives low to ')
        low_receiver, high_receiver = rest.split(' and high to ')
        return GiveValueCommand(giver, low_receiver, high_receiver)
    return ''

def apply_command(command, bots, outputs):
    if isinstance(command, InitialValueCommand):
        if command.bot not in bots:
            bots[command.bot] = Bot(command.bot)
        bots[command.bot].receive_value(command.value)

    elif isinstance(command, GiveValueCommand):
        if command.giver not in bots:
            bots[command.giver] = Bot(command.giver)
            return False
        giver = bots[command.giver]
        if len(giver.values) < 2:
            return False
        high = giver.high()
        low = giver.low()
        if [low, high] == [17, 61]:
            print 'part 1 : %s' % (command.giver)
        hr = command.high_receiver
        lr = command.low_receiver
        if hr.startswith('bot'):
            if hr not in bots:
                bots[hr] = Bot(hr)
            bots[hr].receive_value(high)
        else:
            if hr not in outputs:
                outputs[hr] = OutputBin(hr)
            outputs[hr].receive_value(high)

        if lr.startswith('bot'):
            if lr not in bots:
                bots[lr] = Bot(lr)
            bots[lr].receive_value(low)
        else:
            if lr not in outputs:
                outputs[lr] = OutputBin(hr)
            outputs[lr].receive_value(low)
    return True

def part_one(commands):
    bots = {}
    outputs = {}


    for command in [ command for command in commands if isinstance(command, InitialValueCommand) ]:
        apply_command(command, bots, outputs)

    retry = deque([ command for command in commands if isinstance(command, GiveValueCommand) ])
    while retry:
        command = retry.popleft()
        if not apply_command(command, bots, outputs):
            retry.append(command)

    return bots, outputs

def part_two(outputs):
    return outputs['output 0'].values[0] * outputs['output 1'].values[0] * outputs['output 2'].values[0]


if __name__ == '__main__':
    # unittest.main()
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
