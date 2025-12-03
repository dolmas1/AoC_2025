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

def find_highest_n_digits(puzzle_input):
    flat_input = [int(x) for xs in puzzle_input for x in xs]
    return len(str(max(flat_input)))

def gen_atoms(n_digits):
    return range(10**(n_digits-1), 10**n_digits)

def generate_candidates(n_digits, all_n = True):
    candidates = []
    for i in range(1, int(n_digits*0.5)+1):
        if n_digits % i == 0:
            num_repeats = int(n_digits / i)
            if all_n or num_repeats == 2:
                for candidate in gen_atoms(i):
                    candidates.append(str(candidate)*num_repeats)
    return candidates

def generate_all_candidates(highest_n_digits, all_n = True):
    all_candidates = []
    for i in range(1, highest_n_digits + 1):
        all_candidates += generate_candidates(i, all_n)
    return set(int(_) for _ in all_candidates)

def solve(puzzle_input):
    highest_n_digits = find_highest_n_digits(puzzle_input)
    pt1_candidates = generate_all_candidates(highest_n_digits, all_n = False)
    pt2_candidates = generate_all_candidates(highest_n_digits, all_n = True)
    ans1 = 0
    ans2 = 0
    for l in puzzle_input:
        this_range = range(int(l[0]), int(l[1]) + 1)
        for i in this_range:
            if i in pt1_candidates:
                ans1 += i
                ans2 += i
            elif i in pt2_candidates:
                ans2 += i
    return ans1, ans2

puzzle_input = parse_input(filename)
ans_1, ans_2 = solve(puzzle_input)

print(ans_1)
print(ans_2)