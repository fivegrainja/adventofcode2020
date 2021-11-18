#! /usr/bin/env python3

"""
Bus schedules
"""

#############
# So it looks like the key to this is the Chinese Remainder
# Theorem - https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
#
# I don't want to implement this until I understand that theorem better,
# so will return to it later.
#############


from pathlib import Path
import time
import math
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

start_time = time.time()
print(f'{start_time=}')
TEST = False
TEST = True

if TEST:
    p = Path(__file__).with_name('day13part1-sample.txt')
else:
    p = Path(__file__).with_name('day13part1-input.txt')

with p.open('r') as f:
    arrival = int(f.readline().strip())
    schedule = f.readline().strip().split(',')

buses = []
for offset, bus in enumerate(schedule):
    if bus != 'x':
        bus = int(bus)
        buses.append((bus, offset))

lcm = math.lcm(*[b[0] for b in buses])
print(f'{lcm=}')


# # Sorting will put the largest bus numb er at the end
# buses.sort()
# print(buses)
# max_bus, offset_of_max_bus = buses.pop()
# print(f'{max_bus=} {offset_of_max_bus=}')

# n = 1
# while True:
#     t = n * max_bus - offset_of_max_bus
#     if t % 1000000000 == 0:
#         print(f'{t=}')
#         print(f'elapsed time is {time.time()-start_time}')
#     for bus, offset in buses:
#         if (t + offset) % bus != 0:
#             break
#     else:
#         # We fell through the loop, so t meets conditions
#         break
#     # Try the next multiple of largest_bus
#     n += 1

# print(f'{t=}')

print(f'elapsed time is {time.time() - start_time}')





