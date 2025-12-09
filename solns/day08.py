#!/usr/bin/env python
from collections import Counter
sample = False

if sample:
    filename = "inputs/day08_sample.txt"
else:
    filename = "inputs/day08.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = [tuple(map(int, l.strip().split(','))) for l in f.readlines()]
    return puzzle_input

puzzle_input = parse_input(filename)


def calc_distance(b1, b2):
    return sum((x - y) ** 2 for x, y in zip(b1, b2))

def list_product(l):
    y = 1
    for p in l:
        y *= p
    return y
    
def solve(puzzle_input, sample):
    if sample:
        n_reps = 10
    else:
        n_reps = 1000
    
    # Pre-calculate distance matrix
    n_boxes = len(puzzle_input)
    distances = {}
    for i in range(n_boxes):
        for j in range(n_boxes):
            if j > i:
                distances[(i, j)] = calc_distance(puzzle_input[i], puzzle_input[j])
    sorted_distances = sorted(distances, key = lambda x: distances[x])
    
    # Allocate starting groups
    groups = {i: i for i in range(n_boxes)}
    # merge groups
    for iteration, (i, j) in enumerate(sorted_distances):
        if iteration == n_reps:
            biggest_groups = sorted(Counter(groups.values()).values())
            
        group_from = groups[i]
        group_to = groups[j]

        ## TODO: THIS BIT!
        for b in range(n_boxes):
            if groups[b] == group_from:
                groups[b] = group_to
        if len(set(groups.values())) == 1:
            break
    ans1 = list_product(biggest_groups[-3:])
    ans2 = puzzle_input[i][0] * puzzle_input[j][0]
    return ans1, ans2

ans1, ans2 = solve(puzzle_input, sample)
print(ans1)
print(ans2)
