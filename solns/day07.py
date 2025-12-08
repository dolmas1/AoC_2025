#!/usr/bin/env python
#from collections import Counter
sample = False

if sample:
    filename = "inputs/day07_sample.txt"
else:
    filename = "inputs/day07.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = [l.strip() for l in f.readlines()[::2]]
    return puzzle_input

puzzle_input = parse_input(filename)

def solve(puzzle_input):
    ans = 0
    ways_to_reach = [int(c == 'S') for c in puzzle_input[0]]
    for l in puzzle_input[1:]:
        splitters = [c == '^' for c in l]
        activated_splitters = [r * s for r, s in zip(ways_to_reach, splitters)]
        ans += sum([a > 0 for a in activated_splitters])

        for i, x in enumerate(activated_splitters):
            if x > 0:
                ways_to_reach[i] = 0 # any ray hitting a splitter does not continue
                ways_to_reach[i-1] += x
                ways_to_reach[i+1] += x

    return ans, sum(ways_to_reach)

ans1, ans2 = solve(puzzle_input)

print(ans1)
print(ans2)
