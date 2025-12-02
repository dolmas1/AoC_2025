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


def solve_pt1(puzzle_input):
    pos = 50
    ans = 0
    for l in puzzle_input:
        if l[0] == 'L':
            x = -1 * int(l[1:])
        else:
            x = int(l[1:])
        pos += x
        pos = pos % 100
        if pos == 0:
            ans += 1
        #print(pos, ans)
    return ans


def solve_pt2(puzzle_input):
    pos = 50
    ans = 0
    for l in puzzle_input:
        x = int(l[1:])
        direc = l[0]

        for i in range(x):
            if direc == 'L':
                pos += -1
                if pos == -1:
                    pos = 99
            else:
                pos += 1
                if pos == 100:
                    pos = 0
            if pos == 0:
                    ans += 1
        #print(pos, ans)
    return ans


puzzle_input = parse_input(filename)
ans_1 = solve_pt1(puzzle_input)
ans_2 = solve_pt2(puzzle_input)

print(ans_1)
print(ans_2)



