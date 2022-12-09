import time


def solution():
    data = open(r'days\9\9.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

movements = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}
    
def part1(data):
    tail_locs = set()
    x, y = 0, 0
    tx, ty = 0, 0
    # tail starts at 0, 0 same as head
    tail_locs.add((tx, ty))
    for line in data:
        direction, amt = line.split(' ')
        amt = int(amt)
        dx, dy = movements.get(direction)
        for i in range(amt):
            x += dx
            y += dy
            if abs(x - tx) > 1 or abs(y - ty) > 1:
                tx = x - dx
                ty = y - dy
                tail_locs.add((tx, ty))
    return len(tail_locs)

def part2(data):
    tail_locs = set()
    knots = {k: (0, 0) for k in range(10)}
    tail_locs.add(knots[9])
    for line in data:
        direction, amt = line.split(' ')
        amt = int(amt)
        dx, dy = movements.get(direction)
        for i in range(amt):
            hx, hy = knots[0]
            hx += dx
            hy += dy
            knots[0] = (hx, hy)
            for kin in range(1, len(knots.keys())):
                current_knot = knots[kin]
                parent = knots[kin - 1]
                distX = parent[0] - current_knot[0]
                distY = parent[1] - current_knot[1]
                offsetX, offsetY = 0, 0
                if abs(distX) + abs(distY) > 2:
                    offsetX = distX // abs(distX) if abs(distX) != 0 else 0
                    offsetY = distY // abs(distY) if abs(distY) != 0 else 0
                elif abs(distX) > 1:
                    offsetX = distX // abs(distX) if abs(distX) != 0 else 0
                    offsetY = 0
                elif abs(distY) > 1:
                    offsetX = 0
                    offsetY = distY // abs(distY) if abs(distY) != 0 else 0
                cx, cy = current_knot
                cx += offsetX
                cy += offsetY
                knots[kin] = (cx, cy)
                if kin == 9:
                    tail_locs.add(knots[kin])
            
    return len(tail_locs)

solution()