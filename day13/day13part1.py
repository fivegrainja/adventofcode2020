#! /usr/bin/env python3

"""
Bus schedules
"""

from pathlib import Path
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day13part1-sample.txt')
else:
    p = Path(__file__).with_name('day13part1-input.txt')

with p.open('r') as f:
    arrival = int(f.readline().strip())
    buses = [int(b) for b in f.readline().strip().split(',') if b != 'x']

print(arrival)
print(buses)

best_bus = buses[0]
best_wait = best_bus - arrival % buses[0]
for bus in buses[1:]:
    this_wait = bus - arrival % bus
    print(f'Bus {bus} has a wait of {this_wait}')
    if this_wait < best_wait:
        best_bus = bus
        best_wait = this_wait


print(f'Bus number {best_bus} has the best wait of only {best_wait} minutes.')
print(f'{best_bus} * {best_wait} is {best_bus*best_wait}')