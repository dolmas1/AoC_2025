#!/usr/bin/env python
import re

sample = False

if sample:
    filename = "inputs/day02_sample.txt"
else:
    filename = "inputs/day02.txt"

def parse_input(filename):
    with open(filename, 'r') as f:
        puzzle_input = [l.strip().split('-') for l in f.read().split(',')]
    return puzzle_input

def solve_pt1(puzzle_input):
    ans = []
    for pairs in puzzle_input:
        for i in range(int(pairs[0]), int(pairs[1])+1):
            x = str(i)
            lenx = len(x)
            
            if lenx % 2 == 0:
                splitpoint = int(lenx / 2)
                leftx = x[:splitpoint]
                rightx = x[splitpoint:]
                if leftx == rightx:
                    ans.append(i)
    return sum(ans)


def solve_pt2(puzzle_input):
    ans = []
    for pairs in puzzle_input:
        for i in range(int(pairs[0]), int(pairs[1])+1):
            x = str(i)
            if re.match(r'^(\d+)\1+$', x):
                #print(i)
                ans.append(i)
    return sum(ans)

puzzle_input = parse_input(filename)
ans_1 = solve_pt1(puzzle_input)
ans_2 = solve_pt2(puzzle_input)

print(ans_1)
print(ans_2)