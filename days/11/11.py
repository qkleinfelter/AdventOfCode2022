import time


def solution():
    data = open(r'days\11\11.in').read().split('\n\n')
    # data = open(r'days\11\ex.in').read().split('\n\n')
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    monkey_items = [[] for _ in range(len(data))]
    operations = []
    divisible_by = []
    throws = []
    for index, monkey in enumerate(data):
        lines = monkey.split('\n')
        lines = [line.strip() for line in lines]
        item_line = lines[1]
        item_line = item_line[item_line.index(':') + 2:]
        this_monkey_items = [int(x.strip()) for x in item_line.split(',')]
        monkey_items[index] = this_monkey_items

        op_line = lines[2]
        op_line = op_line[op_line.index('= old') + 2:]
        operations.append(op_line)

        test_line = lines[3]
        divisor = int(test_line.split(' ')[-1])
        divisible_by.append(divisor)

        true_line = lines[4]
        false_line = lines[5]
        true_throw = int(true_line.split(' ')[-1])
        false_throw = int(false_line.split(' ')[-1])
        throws.append((true_throw, false_throw))
    
    num_inspects = [0 for _ in range(len(data))]
    for rd_num in range(20):
        for monkey_index, monkey in enumerate(monkey_items):
            for item in monkey:
                this_operation = operations[monkey_index]
                spl_op = this_operation.split(' ')
                other_num = int(spl_op[-1]) if spl_op[-1] != 'old' else item
                operator = spl_op[-2]
                num_inspects[monkey_index] += 1
                new_item = item * other_num if operator == '*' else item + other_num
                new_item = new_item // 3

                divisor_to_check = divisible_by[monkey_index]
                new_monkey = throws[monkey_index][0 if new_item % divisor_to_check == 0 else 1]
                monkey_items[new_monkey].append(new_item)
                monkey_items[monkey_index] = monkey_items[monkey_index][1:]

    num_inspects.sort(reverse=True)
    return num_inspects[0] * num_inspects[1]

def part2(data):
    monkey_items = [[] for _ in range(len(data))]
    operations = []
    divisible_by = []
    throws = []
    for index, monkey in enumerate(data):
        lines = monkey.split('\n')
        lines = [line.strip() for line in lines]
        item_line = lines[1]
        item_line = item_line[item_line.index(':') + 2:]
        this_monkey_items = [int(x.strip()) for x in item_line.split(',')]
        monkey_items[index] = this_monkey_items

        op_line = lines[2]
        op_line = op_line[op_line.index('= old') + 2:]
        operations.append(op_line)

        test_line = lines[3]
        divisor = int(test_line.split(' ')[-1])
        divisible_by.append(divisor)

        true_line = lines[4]
        false_line = lines[5]
        true_throw = int(true_line.split(' ')[-1])
        false_throw = int(false_line.split(' ')[-1])
        throws.append((true_throw, false_throw))
    
    lcm = 1
    for x in divisible_by:
        lcm = (lcm * x)

    num_inspects = [0 for _ in range(len(data))]
    for rd_num in range(10000):
        for monkey_index, monkey in enumerate(monkey_items):
            for item in monkey:
                this_operation = operations[monkey_index]
                spl_op = this_operation.split(' ')
                other_num = int(spl_op[-1]) if spl_op[-1] != 'old' else item
                operator = spl_op[-2]
                num_inspects[monkey_index] += 1
                new_item = item * other_num if operator == '*' else item + other_num
                new_item %= lcm

                divisor_to_check = divisible_by[monkey_index]
                new_monkey = throws[monkey_index][0 if new_item % divisor_to_check == 0 else 1]
                monkey_items[new_monkey].append(new_item)
                monkey_items[monkey_index] = monkey_items[monkey_index][1:]

    num_inspects.sort(reverse=True)
    return num_inspects[0] * num_inspects[1]

solution()