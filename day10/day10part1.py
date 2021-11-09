#! /usr/bin/env python3

"""
Chain of joltage adapters
"""

from pathlib import Path
import collections

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day10part1-sample.txt')
    expected_result_for_1 = 22
    expected_result_for_3 = 10
else:
    p = Path(__file__).with_name('day10part1-input.txt')

with p.open('r') as f:
    adapters = [int(l) for l in f.readlines() if l.strip()]

adapters.append(0) # This represents the charging port
adapters.sort()
adapters.append(adapters[-1]+3) # This represents the device being charged

# differences is a list of the joltage steps between each adjancent adapter
differences = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
# Counter is a quick way of tallying the various values in differences list.
counts = collections.Counter(differences)

result = counts[1] * counts[3]
print(f'Number of 1 jolt differences is {counts[1]}')
print(f'Number of 3 jolt differences is {counts[3]}')
print(f'Product of those is {result}')

if TEST:
    assert(counts[1] == expected_result_for_1)
    assert(counts[3] == expected_result_for_3)
    print('Test SUCCESS')

