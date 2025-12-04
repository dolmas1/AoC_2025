#!/usr/bin/env python
sample = False

if sample:
    filename = "inputs/day01_sample.txt"
else:
    filename = "inputs/day01.txt"

def parse_input(filename):
    with open(filename, 'r') as f:
        puzzle_input = [l.strip() for l in f.readlines()]
    return puzzle_input

def solve(puzzle_input):
    pos = 50
    ans1 = 0
    ans2 = 0
    for l in puzzle_input:
        x = int(l[1:])
        #print('\n', l[0], x)

        div, x = divmod(x, 100)
        if div > 0:
            #print(div)
            ans2 += div
        if l[0] == 'L':
            x = -x

        new_pos = pos + x
        newer_pos = new_pos % 100
        if ((newer_pos != new_pos) & (pos > 0)):
            ans2 += 1
        elif newer_pos == 0:
            ans2 += 1
        if newer_pos == 0:
            ans1 += 1
        pos = newer_pos

    return ans1, ans2

puzzle_input = parse_input(filename)
ans_1, ans_2 = solve(puzzle_input)

print(ans_1)
print(ans_2)



