def solution():
    data = open(r'days\3\3.in').readlines()
    data = [x.strip() for x in data]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    sum = 0
    for line in data:
        first_half = line[0:(len(line) // 2)]
        second_half = line[len(line) // 2:]
        for char in first_half:
            if char in second_half:
                score = ord(char) - ord('a') + 1
                if score < 0:
                    score += 58
                sum += score
                break
    return sum

def part2(data):
    sum = 0
    i = 0
    while i < len(data) - 2:
        line_one, line_two, line_three = data[i], data[i+1], data[i+2]
        for char in line_one:
            if char in line_two and char in line_three:
                score = ord(char) - ord('a') + 1
                if score < 0:
                    score += 58
                sum += score
                break
        i += 3
    
    return sum

solution()
