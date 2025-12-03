#!/usr/bin/env python
sample = False

if sample:
    filename = "inputs/day03_sample.txt"
else:
    filename = "inputs/day03.txt"

def parse_input(filename):
    with open(filename, 'r') as f:
        puzzle_input = [l.strip() for l in f.readlines()]
    return puzzle_input


def solve_pt1(puzzle_input):
    ans = 0
    for l in puzzle_input:
        first_digit = l[0]
        first_digit_pos = 0
        
        # find the first digit
        for i, digit in enumerate(l[1:-1]):
            if digit > first_digit:
                first_digit = digit
                first_digit_pos = i+1
                
        # find the second digit
        second_digit = l[first_digit_pos + 1]
        if first_digit_pos + 1 < len(l):
            for digit in l[first_digit_pos + 1:]:
                if digit > second_digit:
                    second_digit = digit
        line_sol = int(first_digit + second_digit)
        ans += line_sol
        
    return ans

def find_peak(l, start_pos, digits_to_spare):
    
    best_digit = l[start_pos]
    best_pos = start_pos
    for i, digit in enumerate(l[start_pos+1:len(l)-digits_to_spare]):
        #print( i, digit)
        if digit > best_digit:
            best_digit = digit
            best_pos = start_pos + 1 + i
            if digit == '9':
                break
    #print(f'finding best dig in {l[start_pos:len(l)-digits_to_spare]}: {best_digit}')
    return best_digit, best_pos

def solve_pt2(puzzle_input, tot_digits = 12):
    ans = 0
    for l in puzzle_input:
        this_ans = ''
        current_pos = -1
        for i in range(0, tot_digits):
            best_digit, current_pos = find_peak(l, start_pos = current_pos + 1, digits_to_spare = tot_digits - (i + 1))
            this_ans += best_digit
    
        ans += int(this_ans)
    return ans

puzzle_input = parse_input(filename)
ans_1 = solve_pt1(puzzle_input)
ans_2 = solve_pt2(puzzle_input)

print(ans_1)
print(ans_2)
