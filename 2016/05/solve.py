#!/usr/bin/env python

import hashlib

def main(lines):
    door_id = lines[0]
    # door_id = 'abc'
    password = ''

    index = 0
    while (len(password) < 8):
        unhashed = door_id + str(index)
        hashed = hashlib.md5(unhashed).hexdigest()

        if is_password_hash(hashed):
            print unhashed
            print hashed
            password += get_password_character(hashed)
            print password
        index += 1

    print password


def is_password_hash(hashed):
    return hashed.startswith('00000')

def get_password_character(hashed):
    return hashed[5]

if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
