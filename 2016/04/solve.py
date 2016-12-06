#!/usr/bin/env python

import operator
import string

class Room(object):
    def __init__(self, name, sector_id, checksum):
        self.name = name
        self.sector_id = sector_id
        self.checksum = checksum

def main(lines):
    real_rooms = get_real_rooms(lines)
    print 'part one : %d' % (sum([r.sector_id for r in real_rooms ]))
    # print [ r.name for r in real_rooms]
    decrypted_rooms = [ Room(rotate(r.name, r.sector_id), r.sector_id, r.checksum) for r in real_rooms]
    # print [ r.name for r in decrypted_rooms ]
    print ''.join([ 'part two : %s - %d' % (r.name, r.sector_id) for r in decrypted_rooms if 'north' in r.name ])




def rotate(name, times):
    rot = times % 26
    alpha = string.ascii_lowercase
    rotated = ''
    for char in name:
        if char == '-':
            rotated += ' '
        else:
            rotated += alpha[(alpha.index(char) + rot) % len(alpha)]
    return rotated


def get_real_rooms(lines):
    real_rooms = []
    for room in lines:
        last_dash = room.rfind('-')
        first_bracket = room.rfind('[')
        last_bracket = room.rfind(']')
        name = room[0:last_dash]
        sector_id = room[last_dash+1:first_bracket]
        checksum = room[first_bracket+1:last_bracket]
        if is_real(name, checksum):
            real_rooms.append(Room(name, int(sector_id), checksum))
    return real_rooms

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
