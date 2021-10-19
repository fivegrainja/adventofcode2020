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

highest_id = 0
for line in lines:
    seat_id = get_seat_id(line)
    if seat_id > highest_id:
        highest_id = seat_id

print(f'Highest sat id is {highest_id}')

# row = get_row('BBFFBBFRLL')
# col = get_column('BBFFBBFRLL')
# seat_id = get_seat_id(row, col)
# print(f'row is {row}')
# print(f'col is {col}')
# print(f'seat id is {seat_id}')



