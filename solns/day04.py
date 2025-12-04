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

    def __str__(self):
      "Method to show something human-readable when print() is called on a grid object"
      return "\n".join(''.join([str(c) for c in row]) for row in self.grid)

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

    def find_removable_rolls(self):
        rolls = []
        for x in range(self.x_max):
            for y in range(self.y_max):
                if self.lookup(x, y) == '@':
                    neighbours = self.get_neighbours(x, y)
                    if Counter(neighbours)['@'] < 4:
                        rolls.append([x, y])
        return rolls

    def remove_rolls(self, roll_locations):
        for [x, y] in roll_locations:
            self.assign(x, y, 'x')
        
    def find_and_remove_rolls(self):
        ans = 0
        for x in range(self.x_max):
            for y in range(self.y_max):
                if self.lookup(x, y) == '@':
                    neighbours = self.get_neighbours(x, y)
                    if Counter(neighbours)['@'] < 4:
                        self.assign(x, y, 'x')
                        ans += 1
        return ans
        
        

        

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
