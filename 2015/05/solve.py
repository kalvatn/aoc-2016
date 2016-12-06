#!/usr/bin/env python

VOWELS = 'aeiou'

def main(lines):
    nice_words = []
    for word in lines:
    # for word in ['aeiouaeiouaeiou', 'aei', 'xazegov', 'aaxxddqqeio', 'ab', 'cd', 'pq', 'xy', 'aaccee', 'ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']:
        vowel_count = 0
        double_found = False
        prev_char = None
        has_illegal = False
        for char in word:
            if prev_char:
                if char == prev_char:
                    double_found = True
                if prev_char + char in ['ab', 'cd', 'pq', 'xy']:
                    has_illegal = True
                    break
            if char in VOWELS:
                vowel_count += 1
            prev_char = char
        if not has_illegal and double_found and vowel_count >= 3:
            nice_words.append(word)
    print len(nice_words)

def part_two(lines):
    # lines = [
    #     'qjhvhtzxzqqjkmpb',
    #     'xxyxx',
    #     'uurcxstgmygtbstg',
    #     'ieodomkazucvgmuy',
    #     'nofhmbxififwroeg'
    # ]

    very_nice = 0
    for word in lines:
        # print word
        if legal_repeats(word):
            very_nice += 1


    print very_nice
    # assert len(all_words['good']) == 2

def legal_repeats(word):
    if all(word[i] != word[i+2] for i in range(len(word) -2)):
        return False
    if all(word.count(str(word[i]+word[i+1])) != 2 for i in range(len(word)-1)):
        return False
    return True

if __name__ == '__main__':
    lines = []
    with open('input') as file:
        for line in file:
            lines.append(line.strip())
    main(lines)
    part_two(lines)
