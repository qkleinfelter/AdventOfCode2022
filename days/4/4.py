def solution():
    data = open(r'days\4\4.in').readlines()
    data = [x.strip() for x in data]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    sum = 0
    for line in data:
        one, two = line.split(',')
        ostart, oend = one.split('-')
        tstart, tend = two.split('-')
        ostart, oend, tstart, tend = int(ostart), int(oend), int(tstart), int(tend)
        if ostart <= tstart <= tend <= oend or tstart <= ostart <= oend <= tend:
            sum += 1
    return sum

def part2(data):
    sum = 0
    for line in data:
        one, two = line.split(',')
        ostart, oend = one.split('-')
        tstart, tend = two.split('-')
        ostart, oend, tstart, tend = int(ostart), int(oend), int(tstart), int(tend)
        if ostart <= tstart <= oend or tstart <= ostart <= tend:
            sum += 1
    return sum


solution()
