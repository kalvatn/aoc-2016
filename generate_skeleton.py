#!/usr/bin/env python

import os
from os import path
from os import makedirs

YEARS = [2015, 2016]


def main():
    for year in YEARS:
        for day in range(1, 25):
            dirpath = '%4d/%02d' % (year, day)
            try:
                makedirs(dirpath)
            except OSError:
                pass
                # print 'directory %s already exists' % (dirpath)


if __name__ == '__main__':
    main()
