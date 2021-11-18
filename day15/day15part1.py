#! /usr/bin/env python3

"""
Repeated numbers
"""

from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)
import collections

TEST = False
# TEST = True

part1_N = 2020
part2_N = 30000000
N = part2_N

if TEST:
    input = "0,3,6"
    success = 436
else:
    input = "5,1,9,18,13,8,0"
input = [int(i) for i in input.split(',')]

nums = collections.defaultdict(list)
for i, num in enumerate(input):
    nums[num].append(i+1) # Adding one since question description uses 1-indexed language
last = input[-1]

for i in range(len(nums)+1, N+1):
    # last has already been put into nums. Figure out what the next value in the sequence is,
    # add it to nums, and set last=[this next value]
    if len(nums[last]) == 1:
        # That was last's first appearance, so next number in sequence is zero
        next = 0
    else:
        next = nums[last][-1] - nums[last][-2]
    # print(f'{i=} {last=} {next=}')
    nums[next].append(i)
    last = next

print(f'{last=}')

