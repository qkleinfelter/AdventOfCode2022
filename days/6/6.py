def solution():
    data = open(r'days\6\6.in').read()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    for i in range(3, len(data), 1):
        char_set = set(data[i-3:i+1])
        if len(char_set) == 4:
            return i + 1

def part2(data):
    for i in range(13, len(data), 1):
        char_set = set(data[i-13:i+1])
        if len(char_set) == 14:
            return i + 1

solution()
