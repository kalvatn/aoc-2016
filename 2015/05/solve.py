#!/usr/bin/env python

from stdlib import aoc

VOWELS = 'aeiou'

class Day5(aoc.Day):
    def __init__(self):
        super(Day5, self).__init__(__file__)

    def run(self):
        self.part_one()
        self.part_two()

    def part_one(self):
        nice_words = []
        for word in self.read_input():
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
        self.log.info('part 1 : %d' % (len(nice_words)))

    def part_two(self):
        lines = self.read_input()
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
            if self.legal_repeats(word):
                very_nice += 1

        self.log.info('part 2 : %d' % (very_nice))

    def legal_repeats(self, word):
        if all(word[i] != word[i+2] for i in range(len(word) -2)):
            return False
        if all(word.count(str(word[i]+word[i+1])) != 2 for i in range(len(word)-1)):
            return False
        return True

if __name__ == '__main__':
    Day5().run()
