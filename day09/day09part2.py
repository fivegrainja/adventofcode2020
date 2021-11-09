#! /usr/bin/env python3

"""
Sum of previous numbers
"""

from pathlib import Path
import sys

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day09part1-sample.txt')
    windowSize = 5
    first_invalid = 127 # answer from part 1
    expected_result = 62
else:
    p = Path(__file__).with_name('day09part1-input.txt')
    windowSize = 25 
    first_invalid = 20874512 # answer from part 1

with p.open('r') as f:
    nums = [int(l) for l in f.readlines() if l.strip()]

valid = [True] * windowSize + [False] * (len(nums)-windowSize)


for i in range(0, len(nums)-1):
    left_num = nums[i]
    sum = left_num

    for j in range(i+1, len(nums)):
        right_num = nums[j]
        sum += right_num
        if sum == first_invalid:
            print(f'left is {left_num}')
            print(f'right is {right_num}')
            print(f'range is {i}-{j}')
            terms = nums[i:j+1]
            terms.sort() # This is a lazy but concise way to determine the two largest numbers.
            print(f'Smallest is {terms[0]}')
            print(f'Largest is {terms[-1]}')
            result = terms[0] + terms[-1]
            print(f'Which add up to {result}')
            
            if TEST:
                if result == expected_result:
                    print('Test SUCCESS')
                else:
                    print('Test FAILED')

print('Completed')
