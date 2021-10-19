#! /usr/bin/env python3

"""
Boarding passes
"""

from pathlib import Path

p = Path(__file__).with_name('day05part1-input.txt')
with p.open('r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

rows = range(128)
def get_row(line):
    row = 0
    for i, half in enumerate(line[:7]):
        if half == 'B':
            row += 2 ** (6-i)
    return row

columns = range(8)
def get_column(line):
    column = 0
    for i, half in enumerate(line[7:]):
        if half == 'R':
            column += 2 ** (2-i)
    return column

def get_seat_id(boarding_pass):
    row = get_row(boarding_pass)
    col = get_column(boarding_pass)
    return row * 8 + col

occupied_seat_ids = set()
for line in lines:
    occupied_seat_ids.add(get_seat_id(line))

all_seat_ids = set(range(1024))
missing_ids = all_seat_ids - occupied_seat_ids
for missing_id in missing_ids:
    if missing_id-1 in occupied_seat_ids and missing_id+1 in occupied_seat_ids:
        print(f'Your seat is {missing_id}')
