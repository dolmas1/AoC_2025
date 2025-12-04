#!/usr/bin/env python
#from collections import Counter
import sys
sys.path.append('utils/')
from grid import Grid

sample = False

if sample:
    filename = "inputs/day04_sample.txt"
else:
    filename = "inputs/day04.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = [[c == '@' for c in l.strip()] for l in f.readlines()]
    return puzzle_input


def solve(puzzle_input):
    grid = Grid(puzzle_input)
    
    rolls = grid.find_removable_rolls()
    ans1 = len(rolls)

    grid.remove_rolls(rolls)

    ans2 = ans1
    while True:
        new_removals = grid.find_and_remove_rolls()
        ans2 += new_removals
        if new_removals == 0:
            break

    return ans1, ans2

puzzle_input = parse_input(filename)
ans_1, ans_2 = solve(puzzle_input)

print(ans_1)
print(ans_2)
