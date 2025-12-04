#!/usr/bin/env python
from collections import Counter
sample = False

if sample:
    filename = "inputs/day04_sample.txt"
else:
    filename = "inputs/day04.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = [l.strip() for l in f.readlines()]
    return puzzle_input


class Grid:
    def __init__(self, puzzle_input):
        if isinstance(puzzle_input[0], list):
            self.grid = puzzle_input
        elif isinstance(puzzle_input[0], str):
            self.grid = [list(l) for l in puzzle_input]
        self.x_max = len(self.grid[0])
        self.y_max = len(self.grid)

    def lookup(self, x, y):
        if x >= self.x_max:
            return None
        elif x < 0:
            return None
        elif y >= self.y_max:
            return None
        elif y < 0:
            return None
        else:
            return self.grid[y][x]

    def assign(self, x, y, val):
        if x >= self.x_max:
            return None
        elif x < 0:
            return None
        elif y >= self.y_max:
            return None
        elif y < 0:
            return None
        else:
            self.grid[y][x] = val
            return None

    def get_neighbours(self, x, y):
        
        neighbour_coords = [[x - 1, y - 1],
                            [x, y - 1],
                            [x + 1, y - 1],
                            [x - 1, y],
                            #[x, y],
                            [x + 1, y],
                            [x - 1, y + 1],
                            [x, y + 1],
                            [x + 1, y + 1],
                           ]
        neighbours = [self.lookup(x, y) for [x, y] in neighbour_coords]
        return [x for x in neighbours if x is not None]

    def count_removable_rolls(self):
        ans = 0
        for x in range(self.x_max):
            for y in range(self.y_max):
                if self.lookup(x, y) == '@':
                    neighbours = self.get_neighbours(x, y)
                    if Counter(neighbours)['@'] < 4:
                        ans += 1
        return ans

    def remove_rolls(self):
        ans = 0
        for x in range(self.x_max):
            for y in range(self.y_max):
                if self.lookup(x, y) == '@':
                    neighbours = self.get_neighbours(x, y)
                    if Counter(neighbours)['@'] < 4:
                        self.assign(x, y, 'x')
                        ans += 1
        return ans
        
        

def solve_pt1(grid):
    return grid.count_removable_rolls()

def solve_pt2(grid):
    ans = 0
    while True:
        new_removals = grid.remove_rolls()
        ans += new_removals
        if new_removals == 0:
            break
    return ans

puzzle_input = parse_input(filename)
grid = Grid(puzzle_input)
ans_1 = solve_pt1(grid)
ans_2 = solve_pt2(grid)

print(ans_1)
print(ans_2)
