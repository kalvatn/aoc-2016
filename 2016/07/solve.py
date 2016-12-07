#!/usr/bin/env python

LB = '['
RB = ']'

def main(lines):
    part1_1 = 0
    part1 = 0
    part2 = 0
    for line in lines:
        supernet = ''
        hypernet = ''
        in_hyper = False
        for i in range(0, len(line)):
            if line[i] in [LB, RB]:
                in_hyper = True if not in_hyper and line[i] == LB else False
            else:
                if in_hyper:
                    hypernet += line[i]
                else:
                    supernet += line[i]
        part1 += part_one(line, supernet, hypernet)
    print 'part 1 : %d' % (part1)
    print 'part 2 : %d' % (part2)

def part_one(line, supernet, hypernet):
    abbas = []
    for i in range(0, len(line) - 3):
        abba = line[i:i+4]
        if abba == len(abba) * abba[0]:
            continue
        if abba[0] != abba[3] or abba[1] != abba[2]:
            continue
        abbas.append(abba)

    if len(abbas) > 0:
        for abba in abbas:
            if abba in hypernet:
                return 0
        return 1
    return 0

if __name__ == '__main__':
    test_input = [
        # 'abba[mnop]qrst', #yes
        # 'abcd[bddb]xyyx', #no
        # 'aaaa[qwer]tyui', #no
        # 'ioxxoj[asdfgh]zxcvbn', #yes
        # 'i[oxxo]j[asdfgh]zxcvbn', #yes
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
