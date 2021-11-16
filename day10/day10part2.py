#! /usr/bin/env python3

"""
Chain of joltage adapters
"""

from pathlib import Path
import collections
from rich import print
import rich.traceback
rich.traceback.install()

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

# Step through each adapter and calculate the total number of combinations for getting to that
# adapter's joltage. This is equal to
# the number of ways to get to (this joltage-3) [note this is 0 if no adapter exists for that joltage]
# + the number of ways to get to (this joltage-2) [note this is 0 if no adapter exists for that joltag]
# + the number of ways to get to (this joltage-3) [yep, same note as above]
#
# combinations is a dictionary where the keys are the adapter joltages and the values are the number
# of combinations of adapters that can reach that joltage.

combinations = {0:1} # We always start at 0 jolts, so there is 1 combination for that joltage
for j in adapters[1:]:
    combinations[j] = combinations.get(j-3, 0) + combinations.get(j-2, 0) + combinations.get(j-1, 0)

print(f'Number of combinations to reach {adapters[-1]} jolts is {combinations[adapters[-1]]}')
