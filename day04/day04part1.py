#! /usr/bin/env python3

"""
How many valid passports?
"""

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

from pathlib import Path

p = Path(__file__).with_name('day04part1-input.txt')
with p.open('r') as f:
    lines = f.readlines()

# Build a list of all passports in the data
# Line by line accumulate data into a passport until a blank line is encountered,
# then start a new passport
passports = []
passport = {}
for line in lines:
    if line.strip():
        for part in line.split():
            k,v = part.split(':')
            if k in passport:
                raise 'Problem'
            passport[k] = v
    elif passport:
        passports.append(passport)
        passport = {}
# Make sure to include the last passport, which might not be followed
# by a blank line.
if passport:
    passports.append(passport)

# Use a set operation to see which passports have all required keys
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid = [p for p in passports if required.issubset(p.keys())]
invalid = [p for p in passports if not required.issubset(p.keys())]

print(f'Num valid is {len(valid)}')
print(f'Num invalid is {len(invalid)}')
print(f'total is {len(passports)}')
