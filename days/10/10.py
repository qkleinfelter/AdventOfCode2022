import time


def solution():
    data = open(r'days\10\10.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ')
    p2_screen = part2(data)
    for line in p2_screen:
        print(''.join(line))
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
    screen = [[' ' for _ in range(40)] for _ in range(6)]
    sum = 0
    for line in data:
        if line == 'noop':
            cycle = run_cycle(cycle, screen, register)
        else:
            # addx V
            reg_inc = int(line.split(' ')[1])

            cycle = run_cycle(cycle, screen, register)
            cycle = run_cycle(cycle, screen, register)
            
            register += reg_inc
    return screen

def run_cycle(cycle, screen, register):
    cycle += 1
    if abs(((cycle - 1) % 40) - register) <= 1:
        screen[(cycle - 1) // 40][(cycle - 1) % 40] = '█'
    return cycle

solution()