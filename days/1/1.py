def solution():
    data = open(r'days\1\1.in').readlines()
    data = [x.strip() for x in data]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    # Determine amount of calories being carried by elf with most carried
    # elves split by line break
    calories = [0]
    elf_index = 0
    for i, x in enumerate(data):
        if x == '':
            elf_index += 1
            calories.append(0)
            continue
        calories[elf_index] += int(x)
    return max(calories)


def part2(data):
    # Determine amount of calories carried by top 3 elves
    calories = [0]
    elf_index = 0
    for i, x in enumerate(data):
        if x == '':
            elf_index += 1
            calories.append(0)
            continue
        calories[elf_index] += int(x)
    calories.sort()
    return calories[-1] + calories[-2] + calories[-3]

solution()
