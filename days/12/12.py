import time


def solution():
    data = open(r'days\12\12.in').readlines()
    # data = open(r'days\12\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

mvmts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
def part1(data):
    grid = []
    for line in data:
        line_arr = []
        for char in line:
            line_arr.append(char)
        grid.append(line_arr)

    start, end = None, None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                start = (r, c)
                grid[r][c] = 'a'
            elif grid[r][c] == 'E':
                end = (r, c)
                grid[r][c] = 'z'
    q = []
    explored = [start]
    parents = {}
    q.append(start)
    while len(q) > 0:
        v = q[0]
        q = q[1:]
        if v == end:
            steps = 0
            currnode = v
            while currnode != start:
                steps += 1
                currnode = parents[currnode]
            return steps
        for dr, dc in mvmts:
            newr, newc = v[0] + dr, v[1] + dc
            if 0 <= newr < len(grid) and 0 <= newc < len(grid[newr]) and ((ord(grid[newr][newc]) - ord(grid[v[0]][v[1]]) <= 1)):
                # valid piece of the grid
                if (newr, newc) not in explored:
                    explored.append((newr, newc))
                    parents[(newr, newc)] = v
                    q.append((newr, newc))

def part2(data):
    # This is a bad way to do part 2, I definitely should not brute force this
    # it takes ~105 seconds to run on my machine with my input because theres a
    # lot of possible starts
    # I will probably come back and clean this up eventually
    grid = []
    for line in data:
        line_arr = []
        for char in line:
            line_arr.append(char)
        grid.append(line_arr)

    possible_starts = []
    end = None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                possible_starts.append((r, c))
                grid[r][c] = 'a'
            elif grid[r][c] == 'E':
                end = (r, c)
                grid[r][c] = 'z'
            elif grid[r][c] == 'a':
                possible_starts.append((r, c))
    
    shortest = 99999999999
    for start in possible_starts:
        q = []
        explored = [start]
        parents = {}
        q.append(start)
        while len(q) > 0:
            v = q[0]
            q = q[1:]
            if v == end:
                steps = 0
                currnode = v
                while currnode != start:
                    steps += 1
                    currnode = parents[currnode]
                if steps < shortest:
                    shortest = steps
            for dr, dc in mvmts:
                newr, newc = v[0] + dr, v[1] + dc
                if 0 <= newr < len(grid) and 0 <= newc < len(grid[newr]) and ((ord(grid[newr][newc]) - ord(grid[v[0]][v[1]]) <= 1)):
                    # valid piece of the grid
                    if (newr, newc) not in explored:
                        explored.append((newr, newc))
                        parents[(newr, newc)] = v
                        q.append((newr, newc))
    return shortest

solution()