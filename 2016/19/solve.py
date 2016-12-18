from stdlib import aoc

class Day19(aoc.Day):
    def __init__(self):
        super(Day19, self).__init__(__file__)

    def run(self):
        lines = self.read_input()

if __name__ == '__main__':
    Day19().run()
