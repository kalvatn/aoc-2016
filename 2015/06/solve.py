#!/usr/bin/env python

from stdlib import aoc

TOGGLE = 'toggle'
TURN_OFF = 'turn off'
TURN_ON = 'turn on'

# WIDTH, HEIGHT = 10, 10
WIDTH, HEIGHT = 1000, 1000

STATE_ON = 1
STATE_OFF = 0

MATRIX = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
MATRIX_2 = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

class Day6(aoc.Day):
    def __init__(self):
        super(Day6, self).__init__(__file__)

    def run(self):
        lines = self.read_input()
        # lines = [
# 'turn on 4,4 through 5,5',
# 'toggle 0,0 through 9,9',
# 'turn off 0,0 through 9,9',
# 'turn on 0,0 through 9,9',
# 'toggle 0,0 through 9,9',
# 'turn on 4,4 through 5,5',
# 'toggle 0,0 through 9,9',
# 'toggle 0,0 through 9,9',
        # ]
        for line in lines:
            command = ''
            for c in [TOGGLE, TURN_OFF, TURN_ON]:
                if line.startswith(c):
                    command = c
            light_range = [x.strip() for x in line.replace(command, '').split('through')]
            start_x, start_y = [int(z.strip()) for z in light_range[0].split(',')]
            end_x, end_y = [int(z.strip()) for z in light_range[1].split(',')]

            # print "%s (%d, %d) -> (%d, %d)" % (command, start_x, start_y, end_x, end_y)

            for row in range(start_x, end_x + 1):
                for col in range(start_y, end_y + 1):
                    current_state = MATRIX[row][col]
                    brightness_change = 0
                    if command == TOGGLE:
                        new_state = STATE_ON if current_state == STATE_OFF else STATE_OFF
                        brightness_change = 2
                    else:
                        new_state = STATE_ON if command == TURN_ON else STATE_OFF
                        brightness_change = 1 if command == TURN_ON else -1
                    MATRIX[row][col] = new_state
                    new_brightness = MATRIX_2[row][col] + brightness_change
                    if new_brightness >= 0:
                        MATRIX_2[row][col] = new_brightness
                    # print "(%d, %d) current %d, command : %s, new : %d" % (row, col, current_state, command, new_state)

            # print 'matrix after'
            # print_matrix(start_x, start_y, end_x, end_y)

        count_on = 0
        sum_brightness = 0
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if MATRIX[x][y] == STATE_ON:
                    count_on += 1
                sum_brightness += MATRIX_2[x][y]




        self.log.info('part 1 : %d' % count_on)
        self.log.info('part 2 : %d' % sum_brightness)
        # print_matrix()


    def print_matrix(row_start=0, row_end=WIDTH, col_start=0, col_end=HEIGHT):
        for x in range (WIDTH):
            row = ''
            for y in range(HEIGHT):
                row += str(MATRIX[x][y]) + ' '
            print row


if __name__ == '__main__':
    Day6().run()
