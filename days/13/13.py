import time


def solution():
    data = open(r'days\13\13.in').read().split('\n\n')
    # data = open(r'days\13\ex.in').read().split('\n\n
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    sum = 0
    for index, line in enumerate(data):
        # because the input is formatted nicely, we can simply eval the rows into our variables
        left, right = [eval(x) for x in line.split('\n')]
        if compare(left, right) < 0:
            sum += index + 1
    return sum

def part2(data):
    packets = []
    # put all the packets into our list that we'll sort later
    for index, line in enumerate(data):
        left, right = [eval(x) for x in line.split('\n')]
        packets.append(left)
        packets.append(right)
    # also add specified divider packets
    packets.append([[2]])
    packets.append([[6]])

    # quick bubble sort
    for i in range(len(packets)):
        for j in range(len(packets) - 1):
            if compare(packets[j], packets[j + 1]) >= 0:
                # not in the correct order so swap em
                temp = packets[j]
                packets[j] = packets[j + 1]
                packets[j + 1] = temp
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

# returns -1 if left < right (correct order)
# returns 1 if left > right (wrong order)
def compare(left, right):
    if type(left) is int and type(right) is int:
        return 0 if left == right else -1 if left < right else 1
    elif type(left) is int and type(right) is list:
        left = [left]
    elif type(left) is list and type(right) is int:
        right = [right]
    lenleft = len(left)
    lenright = len(right)

    for ll, rr in zip(left, right):
        result = compare(ll, rr)
        if result != 0:
            return result
    if lenleft < lenright:
        return -1
    elif lenleft == lenright:
        return 0
    else:
        return 1
        
solution()