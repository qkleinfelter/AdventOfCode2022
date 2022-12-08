import time


def solution():
    data = open(r'days\8\8.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    trees = []
    for line in data:
        row = [int(char) for char in line]
        trees.append(row)
    
    outer_trees = (len(trees) - 1) * 2 + (len(trees[0]) - 1) * 2
    sum = outer_trees
    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[x]) - 1):
            top_trees = []
            currx = x - 1
            while currx >= 0:
                top_trees.append(trees[currx][y])
                currx -= 1
            if len(top_trees) > 0 and max(top_trees) < trees[x][y]:
                sum += 1
                continue
            left_trees = []
            curry = y - 1
            while curry >= 0:
                left_trees.append(trees[x][curry])
                curry -= 1
            if len(left_trees) > 0 and max(left_trees) < trees[x][y]:
                sum += 1
                continue
            right_trees = []
            curry = y + 1
            while curry < len(trees[x]):
                right_trees.append(trees[x][curry])
                curry += 1
            if len(right_trees) > 0 and max(right_trees) < trees[x][y]:
                sum += 1
                continue
            bottom_trees = []
            currx = x + 1
            while currx < len(trees):
                bottom_trees.append(trees[currx][y])
                currx += 1
            if len(bottom_trees) > 0 and max(bottom_trees) < trees[x][y]:
                sum += 1
                continue
    return sum

def part2(data):
    trees = []
    for line in data:
        row = [int(char) for char in line]
        trees.append(row)
    
    scenic_scores = [[0 for _ in data[0]] for _ in data]
    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[x]) - 1):
            top_score = 0
            currx = x - 1
            while currx >= 0:
                new_tree = trees[currx][y]
                currx -= 1
                top_score += 1
                if new_tree >= trees[x][y]:
                    break
            left_score = 0
            curry = y - 1
            while curry >= 0:
                new_tree = trees[x][curry]
                curry -= 1
                left_score += 1
                if new_tree >= trees[x][y]:
                    break
            right_score = 0
            curry = y + 1
            while curry < len(trees[x]):
                new_tree = trees[x][curry]
                curry += 1
                right_score += 1
                if new_tree >= trees[x][y]:
                    break
            bottom_score = 0
            currx = x + 1
            while currx < len(trees):
                new_tree = trees[currx][y]
                currx += 1
                bottom_score += 1
                if new_tree >= trees[x][y]:
                    break
            scenic_scores[x][y] = top_score * left_score * right_score * bottom_score
    max = -1
    for x in range(1, len(scenic_scores) - 1):
        for y in range(1, len(scenic_scores[x]) - 1):
            if scenic_scores[x][y] > max:
                max = scenic_scores[x][y]
    return max

solution()