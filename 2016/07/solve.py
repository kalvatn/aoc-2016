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
        part2 += part_two(line, supernet, hypernet)
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

def get_sequences_from_net(net):
    sequences = set()

    for i in range(0, len(net) - 2):
        aba = net[i:i+3]
        if len(aba) < 3:
            continue
        if aba == len(aba) * aba[0]:
            continue
        if aba[0] != aba[2] or aba[1] == aba[0]:
            continue
        sequences.add(aba)
    return sequences

def part_two(line, supernet, hypernet):
    abas = get_sequences_from_net(supernet)
    babs = get_sequences_from_net(hypernet)

    if not abas or not babs:
        return 0

    for bab in babs:
        aba = bab[1] + bab[0] + bab[1]
        if aba in abas:
            return 1

    return 0


if __name__ == '__main__':
    test_input = [
        # 'abba[mnop]qrst', #yes
        # 'abcd[bddb]xyyx', #no
        # 'aaaa[qwer]tyui', #no
        # 'ioxxoj[asdfgh]zxcvbn', #yes
        # 'i[oxxo]j[asdfgh]zxcvbn', #yes
        # 'aba[bab]xyz', # yes
        # 'xyx[xyx]xyx', # no
        # 'aaa[kek]eke', # yes
        # 'zazbz[bzb]cdb', # yes
    ]
    lines = []
    if test_input:
        lines = test_input
    else:
        with open('input') as file:
            for line in file:
                lines.append(line.strip())
    main(lines)
