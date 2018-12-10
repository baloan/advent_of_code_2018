#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 8 

459 players; last marble is worth 71790 points
"""

from collections import defaultdict
from pathlib import Path
from pprint import pprint


def part_one():
    #===========================================================================
    # inp = Path(r"day9_input.txt")
    # with inp.open() as fh:
    #     for raw_line in fh:
    #         line = raw_line.rstrip()
    #         s_tokens = line.split(" ")
    #         tokens = [int(t) for t in s_tokens]
    #===========================================================================
    scores = [0] * 459
    marbles = list(range(1, 7179000 + 1))
    circle = [ 0 ]
    current = 0
    while len(marbles):
        for n, score in enumerate(scores):
            if len(marbles) == 0:
                break
            marble = marbles.pop(0)
            if marble > 0 and marble % 23 == 0:
                scores[n] += marble
                remove_at = counter_clockwise_seven(current, len(circle))
                scores[n] += circle.pop(remove_at)
                current = remove_at
            else:
                insert_at = clockwise_one(current, len(circle))
                circle.insert(insert_at, marble)
                current = insert_at
            # print(f"{n:2} {current:2}", circle)
    print(scores)
    print(max(scores))


def clockwise_one(i, m):
    i += 1
    if i >= m:
        i = 0
    return i + 1


def counter_clockwise_seven(i, m):
    i -= 7
    if i < 0:
        i += m
    return i 


if __name__ == '__main__':
    part_one()
