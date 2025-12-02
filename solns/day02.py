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

def solve(puzzle_input):
    ans1 = []
    ans2 = []

    for pairs in puzzle_input:
        for i in range(int(pairs[0]), int(pairs[1])+1):
            x = str(i)
            lenx = len(x)
            
            # Part 1
            if lenx % 2 == 0:
                splitpoint = int(lenx / 2)
                leftx = x[:splitpoint]
                rightx = x[splitpoint:]
                if leftx == rightx:
                    ans1.append(i)

            # Part 2
            if re.match(r'^(\d+)\1+$', x):
                #print(i)
                ans2.append(i)

    return sum(ans1), sum(ans2)


puzzle_input = parse_input(filename)
ans_1, ans_2 = solve(puzzle_input)

print(ans_1)
print(ans_2)