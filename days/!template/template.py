import time


def solution():
    data = open(r'days\{CHANGEME}\{CHANGEME}.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    return 'Not impl'

def part2(data):
    return 'Not impl'

solution()