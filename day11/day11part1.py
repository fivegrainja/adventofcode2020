#! /usr/bin/env python3

"""
Seating evolution
"""

from pathlib import Path
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day11part1-sample.txt')
else:
    p = Path(__file__).with_name('day11part1-input.txt')

with p.open('r') as f:
    # My first time using an assignment expression in a list comprehension,
    # I'm pretty excited about this.
    seats = [list(row) for l in f.readlines() if (row:=l.strip()) != '']

print('Initial seating')
print(seats)

def get_adjacent_seats(seats, row, col):
    """ Return an array of characters representing the seating state of each of the seats
    adjacent to seat row,col
    """
    neighbors = []
    num_rows = len(seats)
    num_cols = len(seats[0])
    # The row above
    if row > 0:
        if col > 0:
            neighbors.append(seats[row-1][col-1])
        neighbors.append(seats[row-1][col])
        if col < num_cols - 1:
            neighbors.append(seats[row-1][col+1])
    # Same row
    if col > 0:
        neighbors.append(seats[row][col-1])
    if col < num_cols - 1:
        neighbors.append(seats[row][col+1])
    # Row below
    if row < num_rows - 1:
        if col > 0:
            neighbors.append(seats[row+1][col-1])
        neighbors.append(seats[row+1][col])
        if col < num_cols - 1:
            neighbors.append(seats[row+1][col+1])
    return neighbors


def get_next_round(seats):
    """ Takes an array of seats, constructs an array representing seating for the next round
    according to the rules of the question.
    Returns a tuple (next_seats, is_different) where next_seats is the next round of seats
    and is_different is a boolean indicating whether any seats changed between seats and next_seats.
    """
    next_seats = []
    is_different = False
    for row in range(len(seats)):
        next_seats.append([])
        for col in range(len(seats[row])):
            this_seat = seats[row][col]
            # Default condition is for the seat's state not to change
            this_seat_becomes = this_seat
            if this_seat == 'L':
                neighbors = get_adjacent_seats(seats, row, col)
                if neighbors.count('#') == 0:
                    this_seat_becomes = '#'
            elif this_seat == '#':
                neighbors = get_adjacent_seats(seats, row, col)
                if neighbors.count('#') >= 4:
                    this_seat_becomes = 'L'
            if this_seat != this_seat_becomes:
                is_different = True
            next_seats[row].append(this_seat_becomes)
    return (next_seats, is_different)

is_different = True
while (is_different):
    seats, is_different = get_next_round(seats)

print('Final seating')
print(seats)

num_occupied = 0
for row in seats:
    num_occupied += row.count('#')
print(f'{num_occupied=}')

            


