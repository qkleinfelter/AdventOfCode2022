def solution():
    data = open(r'days\5\5.in').read().split('\n\n')
    data = [x.split('\n') for x in data]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    stack_lines = data[0]
    instr_lines = data[1]
    stacks = [[] for x in range(0, len(stack_lines[0]) // 4 + 1)]
    for line in stack_lines:
        if line[1] == '1':
            break
        for i in range(0, len(line) // 4 + 1):
            current_char = line[i * 4 + 1]
            if current_char != ' ':
                stacks[i].insert(0, line[i * 4 + 1])

    for instr in instr_lines:
        instr = instr.split(' ')
        for i in range(0, int(instr[1])):
            from_stack = int(instr[3]) - 1
            to_stack = int(instr[5]) - 1
            stacks[to_stack].append(stacks[from_stack].pop())

    result = ''
    for stack in stacks:
        result += stack[-1]
    return result

def part2(data):
    stack_lines = data[0]
    instr_lines = data[1]
    stacks = [[] for x in range(0, len(stack_lines[0]) // 4 + 1)]
    for line in stack_lines:
        if line[1] == '1':
            break
        for i in range(0, len(line) // 4 + 1):
            current_char = line[i * 4 + 1]
            if current_char != ' ':
                stacks[i].insert(0, line[i * 4 + 1])

    for instr in instr_lines:
        instr = instr.split(' ')
        amount_to_move = int(instr[1])
        from_stack = int(instr[3]) - 1
        to_stack = int(instr[5]) - 1
        initial_height = len(stacks[to_stack])
        for i in range(0, amount_to_move):
            from_stack = int(instr[3]) - 1
            to_stack = int(instr[5]) - 1
            stacks[to_stack].insert(initial_height, stacks[from_stack].pop())
    result = ''
    for stack in stacks:
        result += stack[-1]
    return result

solution()
