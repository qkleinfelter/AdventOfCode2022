import time
from collections import defaultdict


def solution():
    data = open(r'days\7\7.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

def part1(data):
    pwd = '/'
    fs = defaultdict(def_value)
    for line in data:
        pieces = line.split(' ')
        if line[0] == '$':
            # Command
            if pieces[1] == 'ls':
                continue
            if pieces[2] == '..':
                pwd = '/'.join(pwd.split('/')[:-2]) + '/'
            else:
                if pieces[2] == '/':
                    pwd = '/'
                else:
                    pwd += pieces[2] + '/'
        else:
            # Result from a cmd
            if pieces[0] != 'dir':
                fs[pwd] += int(pieces[0])
                copied_dir = pwd
                if pwd != '/':
                    while True:
                        one_up = '/'.join(copied_dir.split('/')[:-2]) + '/'
                        fs[one_up] += int(pieces[0])
                        if one_up == '/':
                            break
                        copied_dir = one_up

    sum = 0
    for directory, size in fs.items():
        if size <= 100000:
            sum += size
    return sum

def part2(data):
    TOTAL_AVAILABLE_SPACE = 70000000
    UPDATE_REQUIRES = 30000000
    pwd = '/'
    fs = defaultdict(def_value)
    for line in data:
        pieces = line.split(' ')
        if line[0] == '$':
            # Command
            if pieces[1] == 'ls':
                continue
            if pieces[2] == '..':
                pwd = '/'.join(pwd.split('/')[:-2]) + '/'
            else:
                if pieces[2] == '/':
                    pwd = '/'
                else:
                    pwd += pieces[2] + '/'
        else:
            # Result from a cmd
            if pieces[0] != 'dir':
                fs[pwd] += int(pieces[0])
                copied_dir = pwd
                if pwd != '/':
                    while True:
                        one_up = '/'.join(copied_dir.split('/')[:-2]) + '/'
                        fs[one_up] += int(pieces[0])
                        if one_up == '/':
                            break
                        copied_dir = one_up
    
    total_used = fs['/']
    total_needed = UPDATE_REQUIRES - (TOTAL_AVAILABLE_SPACE - total_used)
    big_enough = []
    for directory, size in fs.items():
        if size > total_needed:
            big_enough.append(size)
    big_enough.sort()
    return big_enough[0]

def def_value():
    return 0

solution()