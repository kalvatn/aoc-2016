#!/usr/bin/env python

import hashlib

def main(lines):
    secret = lines[0]
    index = 0
    print secret
    while True:
        digest = hashlib.md5(secret + str(index)).hexdigest()
        if digest.startswith('00000'):
            break
        index += 1
    print index



if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
