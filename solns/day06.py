#!/usr/bin/env python
#from collections import Counter
sample = False

if sample:
    filename = "inputs/day06_sample.txt"
else:
    filename = "inputs/day06.txt"

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.replace('\n', '') for l in f.readlines()]
    return lines

def parse_pt1(puzzle_input):
    lines = [[c for c in line.split(' ') if c != ''] for line in puzzle_input]
    return lines

def solve_pt1(processed_pt1):
    ans = 0
    for c in range(len(processed_pt1[0])):
        operation = processed_pt1[-1][c]
        arr = [int(l[c]) for l in processed_pt1[:-1]]
        
        if operation == '+':
            ans += sum(arr)
        else:
            product = arr[0]
            for a in arr[1:]:
                product *= a
            ans += product
    return ans

def get_vertical_nums(puzzle_input, idx_range):
    nums = []
    for i in range(idx_range[0], idx_range[1]):
        this_num = int(''.join([l[i] for l in puzzle_input[:-1] if l[i] != ' ']))
        nums.append(this_num)
    return nums

def solve_pt2(puzzle_input):
    add_idx = []
    mult_idx = []
    for i, c in enumerate(puzzle_input[-1]):
        if c == '+':
            add_idx.append(i)
        elif c == '*':
            mult_idx.append(i)
    column_idx = sorted(add_idx + mult_idx + [len(puzzle_input[-1]) + 1])
    add_idx = [[idx, column_idx[column_idx.index(idx)+1]-1] for idx in add_idx]
    mult_idx = [[idx, column_idx[column_idx.index(idx)+1]-1] for idx in mult_idx]

    ans = 0
    for idx_range in add_idx:
        nums = get_vertical_nums(puzzle_input, idx_range)
        ans += sum(nums)
    for idx_range in mult_idx:
        nums = get_vertical_nums(puzzle_input, idx_range)
        this_product = nums[0]
        for n in nums[1:]:
            this_product *= n
        ans += this_product
    return ans



puzzle_input = read_input(filename)

processed_pt1 = parse_pt1(puzzle_input)
ans1 = solve_pt1(processed_pt1)
ans2 = solve_pt2(puzzle_input)

print(ans1)
print(ans2)
