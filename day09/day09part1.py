#! /usr/bin/env python3

"""
Sum of previous numbers
"""

from pathlib import Path
import collections

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day09part1-sample.txt')
    windowSize = 5
else:
    p = Path(__file__).with_name('day09part1-input.txt')
    windowSize = 25 

with p.open('r') as f:
    nums = [int(l) for l in f.readlines() if l.strip()]

# valid is a list the same length as num. When we validate the i-th number in nums we set
# valid[i] to True. This is how we track which nums have been validated or not.
valid = [True] * windowSize + [False] * (len(nums)-windowSize)

# Loop through every number in the list.
# Start by seeing if this number itself has been validated by preceeding numbers. If not then we've
# found an invalid number. (The first windowSize-th numbers start as validated, these are called the
# preamble in the language of the AoC problem.)
# If this number is valid, see if the sum of this number and any of the following numbers within the
# windowSize are present within the list - and if so mark that sum as valid.
# The nested loops can be difficult to keep track of. Here's what's going on:
#
# First loop: i
# This is the current working number (this_num). We loop through every number in the list with this.
#
#    Second loop: j
#    We want to generate sums from this_num (from the outer loop) with the next several items in the
#    list. j starts as the number immediately after this_num (i+1) and goes up to the last number in
#    the sliding window. (i.e. the last number we would add to this_num to validate another number.)
#
#        Third loop: k
#        Given a sum from the number in the outer loop (this_num) and a following number from the second
#        loop, check to see if that sum exists later in the list. We only check numbers in the list
#        that come after the number from the second loop. And we only check as far as the windowSize-th
#        number after this_num.
#
# Potential improvement - Implementing the 2nd and 3rd loops as standalone functions with nicely
# descriptive names would probably help readability a lot, maybe at the expense of a little performance
# hit due to the function calls.

for i in range(len(nums)):
    this_num = nums[i]
    print('----------------')
    print(f'this_num is {this_num}')
    # If this number is not valid then exit
    if not valid[i]:
        print(f'Index {i} with value {this_num} is invalid')
        break
    # Try adding this num to the next (windowSize-1)th numbers in the list
    # And compare those sums to the next (windowSize)th numbers to validate them
    print(f'Looping j from {i+1} to {i+windowSize-1}')
    for j in range(i+1, i+windowSize): # start with i+1 so we don't add this num to itself
        sum = this_num + nums[j]
        print(f'{this_num} + {nums[j]} (index={j}) is {sum}')
        # See if this sum is in nums starting at (j+1)th and ending at (i+windowSize+1)th number
        print(f'Looping k from {j+1} to {i+windowSize+1}')
        for k in range(j+1, i+windowSize+1):
            print(f'Maybe validate index {k} value {nums[k]}')
            if sum == nums[k]:
                print('validated')
                valid[k] = True

if TEST:
    print(f'Result: {this_num}')
    print(f'Correct result: 127')
    if this_num == 127:
        print('SUCCESS')
    else:
        print('FAILED')
else:
    print(f'Completed')
