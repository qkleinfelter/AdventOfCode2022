import time


def solution():
    data = open(r'days\10\10.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    cycle = 0
    register = 1
    important_cycles = [20, 60, 100, 140, 180, 220]
    sum = 0
    for line in data:
        if line == 'noop':
            cycle += 1
            if cycle in important_cycles:
                sum += cycle * register
            continue
        else:
            # addx V
            reg_inc = int(line.split(' ')[1])
            cycle += 1
            if cycle in important_cycles:
                sum += cycle * register
            cycle += 1
            if cycle in important_cycles:
                sum += cycle * register
            register += reg_inc
    return sum

def part2(data):
    cycle = 0
    register = 1
    screen = [['' for _ in range(40)] for _ in range(6)]
    sum = 0
    ln = 0
    for line in data:
        if line == 'noop':
            cycle += 1
            if register - 1 <= cycle % 40 <= register + 1:
                screen[ln][cycle % 40] = '#'
            else:
                screen[ln][cycle % 40] = '.'
            if cycle % 40 == 0:
                ln += 1
        else:
            # addx V
            reg_inc = int(line.split(' ')[1])

            cycle += 1
            if register - 1 <= cycle % 40 <= register + 1:
                screen[ln][cycle % 40] = '#'
            else:
                screen[ln][cycle % 40] = '.'
            if cycle % 40 == 0:
                ln += 1
            
            cycle += 1
            if register - 1 <= cycle % 40 <= register + 1:
                screen[ln][cycle % 40] = '#'
            else:
                screen[ln][cycle % 40] = '.'
            if cycle % 40 == 0:
                ln += 1
            register += reg_inc
    for line in screen:
        print(''.join(line))

solution()