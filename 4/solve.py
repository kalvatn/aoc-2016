#!/usr/bin/env python

def main(lines):
    for room in lines:
        last_dash = room.rfind('-')
        first_bracket = room.rfind('[')
        last_bracket = room.rfind(']')
        name = room[0:last_dash]
        sector_id = room[last_dash+1:first_bracket]
        checksum = room[first_bracket+1:last_bracket]
        print room
        print name
        print sector_id
        print checksum



if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
