def solution():
    data = open(r'days\2\2.in').readlines()
    data = [x.strip() for x in data]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    score = 0
    # A & X = Rock - 1
    # B & Y = Paper - 2
    # C & Z = Scissors - 3
    # 0 L
    # 3 D
    # 6 W
    for x in data:
        opp, me = x.split(' ')
        if me == 'X':
            score += 1
            if opp == 'A':
                score += 3
            elif opp == 'B':
                score += 0
            elif opp == 'C':
                score += 6
        elif me == 'Y':
            score += 2
            if opp == 'A':
                score += 6
            elif opp == 'B':
                score += 3
            elif opp == 'C':
                score += 0
        elif me == 'Z':
            score += 3
            if opp == 'A':
                score += 0
            elif opp == 'B':
                score += 6
            elif opp == 'C':
                score += 3
    return score

def part2(data):
    score = 0
    for x in data:
        # X = Lose
        # Y = Draw
        # X = Win
        opp, ending = x.split(' ')
        if ending == 'X':
            if opp == 'A':
                score += 3
            elif opp == 'B':
                score += 1
            elif opp == 'C':
                score += 2
        elif ending == 'Y':
            score += 3
            if opp == 'A':
                score += 1
            elif opp == 'B':
                score += 2
            elif opp == 'C':
                score += 3
        elif ending == 'Z':
            score += 6
            if opp == 'A':
                score += 2
            elif opp == 'B':
                score += 3
            elif opp == 'C':
                score += 1
    return score

solution()
