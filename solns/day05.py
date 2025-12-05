#!/usr/bin/env python
#from collections import Counter
sample = False

if sample:
    filename = "inputs/day05_sample.txt"
else:
    filename = "inputs/day05.txt"

def parse_input(filename):
    ranges = []
    ingredients = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            if '-' in l:
                ranges.append([int(_) for _ in l.strip().split('-')])
            elif l.strip() == '':
                pass
            else:
                ingredients.append(int(l.strip()))
    return ranges, ingredients


def solve_pt1(ranges, ingredients):
    ans = 0
    for i in ingredients:
        for r in ranges:
            if (i >= r[0]) & (i <= r[1]):
                ans += 1
                break
    return ans

def merge_ranges(r1, r2):
    output = False
    
    # r1 inside r2
    if (r1[0] >= r2[0]) and (r1[1] <= r2[1]):
        output = r2
        
    # r2 inside r1
    elif (r1[0] <= r2[0]) and (r1[1] >= r2[1]):
        output = r1
        
    # r1 is left overlap
    elif (r1[0] <= r2[0]) and (r1[1] >= r2[0]):
        output = [r1[0], r2[1]]

    # r2 is right overlap
    elif (r1[1] >= r2[1]) and (r1[0] <= r2[1]):
        output = [r2[0], r1[1]]

    return output

def merge_all(ranges):
    for i in range(0, len(ranges) - 1):
        for j in range(i+1, len(ranges)):
            merged_range = merge_ranges(ranges[i], ranges[j])
            if merged_range:
                return (False, ranges[:i] + ranges[i+1:j] + ranges[j+1:] + [merged_range])
    return (True, ranges)

def solve_pt2(ranges):
    finished = False
    while not finished:
        finished, ranges = merge_all(ranges)
    
    ans = 0
    for r in ranges:
        ans += (1 + r[1] - r[0])
    return ans, ranges


ranges, ingredients = parse_input(filename)
ans_2, ranges = solve_pt2(ranges)
ans_1 = solve_pt1(ranges, ingredients)


print(ans_1)
print(ans_2)
