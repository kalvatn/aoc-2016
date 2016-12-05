#!/usr/bin/env python

import operator

def main(lines):
    real_rooms = []
    for room in lines:
        last_dash = room.rfind('-')
        first_bracket = room.rfind('[')
        last_bracket = room.rfind(']')
        name = room[0:last_dash]
        sector_id = room[last_dash+1:first_bracket]
        checksum = room[first_bracket+1:last_bracket]
        if is_real(name, checksum):
            real_rooms.append(int(sector_id))
    print sum(real_rooms)

def is_real(name, checksum):
    counts_by_letter = group_letters_by_count(name)
    letters_by_counts = {}
    for k, v in counts_by_letter.items():
        if v not in letters_by_counts:
            letters_by_counts[v] = []
        letters_by_counts[v].append(k)

    counts_sorted = sorted(letters_by_counts.keys())
    counts_sorted.reverse()
    correct_hash = ''
    for count in counts_sorted:
        correct_hash += ''.join(sorted(letters_by_counts[count]))

    return correct_hash.startswith(checksum)

def group_letters_by_count(name):
    counts_by_letter = {}
    for char in name.replace('-',''):
        if not char in counts_by_letter:
            counts_by_letter[char] = 0
        counts_by_letter[char] += 1
    return counts_by_letter


if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
