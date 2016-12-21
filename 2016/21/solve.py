from stdlib import aoc
from stdlib import stringutils
import re

class Day21(aoc.Day):
    def __init__(self):
        super(Day21, self).__init__(__file__)

    def scramble(self, password, unscramble=False):

        swap_pos = re.compile(r'swap position (\d) with position (\d)')
        swap_letter = re.compile(r'swap letter (\w) with letter (\w)')
        rotate_by_steps = re.compile(r'rotate (left|right) (\d) steps?')
        rotate_by_letter = re.compile(r'rotate based on position of letter (\w)')
        reverse_range = re.compile(r'reverse positions (\d) through (\d)')
        move_letter = re.compile(r'move position (\d) to position (\d)')

        lines = self.read_input()
        if unscramble:
            lines = reversed(lines)
        for line in lines:
            before = password
            if swap_pos.match(line):
                from_index, to_index = swap_pos.match(line).groups()
                # self.log.debug('%s -> SWAP pos %d and %d' % (line, int(from_index), int(to_index)))
                if unscramble:
                    from_index, to_index = to_index, from_index
                password = stringutils.swap_index(password, int(from_index), int(to_index))
            elif swap_letter.match(line):
                x, y = swap_letter.match(line).groups()
                # self.log.debug('%s -> SWAP letter %s and %s' % (line, x, y))
                if unscramble:
                    x, y = y, x
                password = stringutils.swap_char(password, x, y)
            elif rotate_by_steps.match(line):
                leftright, x = rotate_by_steps.match(line).groups()
                x = int(x)
                if leftright == 'left':
                    x *= -1
                # self.log.debug('%s -> ROTATE %s %d times' % (line, leftright, int(x)))
                if unscramble:
                    x *= -1
                password = stringutils.rotate(password, x)
            elif rotate_by_letter.match(line):
                x = rotate_by_letter.match(line).groups()[0]
                # self.log.debug('%s -> ROTATE by letter %s' % (line, x))

                if unscramble:
                    index = password.index(x)
                    original_positions_from_current_index = {0: 7, 1: 0, 2: 4, 3: 1, 4: 5, 5: 2, 6: 6, 7: 3}
                    num_rotations = original_positions_from_current_index[index] - index
                else:
                    index = password.index(x)
                    num_rotations = 1 + index
                    if index >= 4:
                        num_rotations += 1

                password = stringutils.rotate(password, num_rotations)
            elif reverse_range.match(line):
                x, y = reverse_range.match(line).groups()
                # self.log.debug('%s -> REVERSE range %d to %d' % (line, int(x), int(y)))
                password = stringutils.reverse_range(password, int(x), int(y))
            elif move_letter.match(line):
                x, y = move_letter.match(line).groups()
                # self.log.debug('%s -> MOVE letter at %d to %d' % (line, int(x), int(y)))
                if unscramble:
                    x, y = y, x
                password = stringutils.move_char(password, int(x), int(y))
            else:
                raise ValueError('invalid instruction %s' % (line))
            if before == password:
                self.log.warn('%s no change' % line)
            if unscramble:
                self.log.debug('UNSCRAMBLE : %s %s -> %s' % (before, line,  password))
            else:
                self.log.debug('SCRAMBLE   : %s %s -> %s' % (before, line,  password))
        return password


    def run(self):
        password = 'abcdefgh'
        part1 = self.scramble(password)
        password = 'fbgdceah'
        part2 = self.scramble(password, unscramble=True)

        self.log.info('part 1 : %s' % (part1))
        self.log.info('part 2 : %s' % (part2))

if __name__ == '__main__':
    Day21().run()
