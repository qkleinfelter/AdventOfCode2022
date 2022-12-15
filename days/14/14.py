import time
from collections import defaultdict


def solution():
    data = open(r'days\14\14.in').readlines()
    # data = open(r'days\14\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    grid = defaultdict(int)
    for line in data:
        spl = line.strip().split(' -> ')
        for i in range(len(spl) - 1):
            coords = spl[i].split(',')
            x, y = int(coords[0]), int(coords[1])
            coords_next = spl[i+1].split(',')
            x2, y2 = int(coords_next[0]), int(coords_next[1])
            dx = x2 - x
            if dx != 0:
                dx = dx // abs(dx)
            dy = y2 - y
            if dy != 0:
                dy = dy // abs(dy)
            while (x, y) != (x2, y2):
                grid[(x, y)] = 1
                x += dx
                y += dy
            grid[(x, y)] = 1
    max_y = max(y for x, y in grid)
    
    sandx, sandy = (500, 0)
    while True:
        blocked = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if grid[(sandx + dx, sandy + dy)] == 0:
                sandx += dx
                sandy += dy
                blocked = False
                break
        if sandy > max_y:
            break
        if blocked:
            grid[(sandx, sandy)] = 2
            if (sandx, sandy) == (500, 0):
                break
            sandx, sandy = (500, 0)
    return sum(1 for v in grid.values() if v == 2)

def part2(data):
    grid = defaultdict(int)
    for line in data:
        spl = line.strip().split(' -> ')
        for i in range(len(spl) - 1):
            coords = spl[i].split(',')
            x, y = int(coords[0]), int(coords[1])
            coords_next = spl[i+1].split(',')
            x2, y2 = int(coords_next[0]), int(coords_next[1])
            dx = x2 - x
            if dx != 0:
                dx = dx // abs(dx)
            dy = y2 - y
            if dy != 0:
                dy = dy // abs(dy)
            while (x, y) != (x2, y2):
                grid[(x, y)] = 1
                x += dx
                y += dy
            grid[(x, y)] = 1
    max_y = max(y for x, y in grid)

    for x in range(-1500, 1500):
        grid[(x, max_y + 2)] = 1
    
    sandx, sandy = (500, 0)
    while True:
        blocked = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if grid[(sandx + dx, sandy + dy)] == 0:
                sandx += dx
                sandy += dy
                blocked = False
                break
        if blocked:
            grid[(sandx, sandy)] = 2
            if (sandx, sandy) == (500, 0):
                break
            sandx, sandy = (500, 0)
    return sum(1 for v in grid.values() if v == 2)

solution()