#!/usr/bin/env python

import hashlib

PASSWORD_LENGTH = 8

def main(lines):
    door_id = lines[0]
    # door_id = 'abc'
    password = ''

    pw1 = ''
    pw2 = [ -1 ] * PASSWORD_LENGTH
    # pw2_char_indexes = [ (0, 'h'), (1, 'e'), (2, 'l'), (3, 'l')]
    pw2_char_indexes = []

    # pw2 = ''
    index = 0

    while (-1 in pw2):
        unhashed = door_id + str(index)
        hashed = hashlib.md5(unhashed).hexdigest()

        if is_password_hash(hashed):
            pw1_char = get_password_character(hashed, 5)
            if pw1_char.isdigit():
                pw2_index = int(pw1_char)
                if pw2_index < PASSWORD_LENGTH and pw2[pw2_index] == -1:
                    pw2[pw2_index] = get_password_character(hashed, 6)
                    print pw2
            if len(pw1) < PASSWORD_LENGTH:
                pw1 += pw1_char
                print 'pw1 %s' % pw1
        index += 1

    print ''.join(pw2)


def is_password_hash(hashed):
    return hashed.startswith('00000')

def get_password_character(hashed, index):
    return hashed[index]

if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
