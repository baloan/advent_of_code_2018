#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 1 """

from pathlib import Path
import sys


def part_one():
    inp = Path(r"day1_input.txt")
    changes = list()
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            changes.append(int(line))
    freq = 0
    for d in changes:
        freq += d
    print(freq)


def part_two():
    inp = Path(r"day1_input.txt")
    changes = list()
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            changes.append(int(line))
    freq = 0
    freqs = set()
    while True:
        for d in changes:
            freq += d
            if freq in freqs:
                print(freq, freqs)
                sys.exit()
            freqs.add(freq)


if __name__ == '__main__':
    part_two()
