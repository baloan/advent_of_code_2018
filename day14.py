#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 14 """

import sys
from pathlib import Path


def part_one():
    recipe_evolution(5)
    recipe_evolution(9)
    recipe_evolution(18)
    recipe_evolution(2018)
    recipe_evolution(409551)


def recipe_evolution(after=9):
    recps = [3, 7]
    elv1 = 0
    elv2 = 1
    while True:
        comb = recps[elv1] + recps[elv2]
        for d in str(comb):
            recps.append(int(d))
        elv1 = step_forward(elv1, recps)
        elv2 = step_forward(elv2, recps)
        # print(elv1, elv2, recps)
        if len(recps) > after + 10:
            break
    print(after, "".join(map(str, recps[after:after + 10])))


def step_forward(n0, recps):
    l = len(recps)
    n1 = n0 + 1 + int(recps[n0])
    n1 = n1 % l
    return n1


def part_two(pattern="409551"):
    recps = "37"
    elv1 = 0
    elv2 = 1
    while pattern not in recps[-7:]:
        comb = int(recps[elv1]) + int(recps[elv2])
        recps += str(comb)
        elv1 = step_forward(elv1, recps)
        elv2 = step_forward(elv2, recps)
    n = recps.index(pattern, len(recps) - 7)
    print(n)


if __name__ == '__main__':
    part_two()
