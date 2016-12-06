#!/usr/bin/env python
import operator

def main(lines):
    lines = [
'eedadn',
'drvtee',
'eandsr',
'raavrd',
'atevrs',
'tsrnev',
'sdttsa',
'rasrtv',
'nssdts',
'ntnada',
'svetve',
'tesnvt',
'vntsnd',
'vrdear',
'dvrsen',
'enarar',
            ]

    words_by_columns = group_words_by_columns(lines)
    error_corrected = ''
    for word in words_by_columns:
        freqs = letter_frequencies(word)
        sorted_by_frequency = sorted(freqs.items(), key=operator.itemgetter(1))
        error_corrected += sorted_by_frequency[-1][0]

    print error_corrected

def group_words_by_columns(words):
    by_columns = []
    for i in range(0,len(words[0])):
        word = ''
        for line in words:
            word += line[i]
        by_columns.append(word)
    return by_columns


def letter_frequencies(word):
    freqs = {}
    for char in word:
        if char not in freqs:
            freqs[char] = 0
        freqs[char] += 1

    return freqs



if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
