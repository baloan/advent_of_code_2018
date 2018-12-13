#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 12 """

STATE0 = "##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####"

TRANSITIONS = {
    "#..#.": "#",
    ".###.": ".",
    "..##.": ".",
    "....#": ".",
    "#...#": ".",
    ".#.#.": ".",
    "#.#.#": "#",
    "#....": ".",
    "#.#..": "#",
    "###.#": ".",
    ".#...": "#",
    "#.###": ".",
    ".#.##": "#",
    "..#..": "#",
    ".####": ".",
    "..###": "#",
    "...#.": ".",
    "##.#.": "#",
    "##.##": "#",
    ".##.#": "#",
    "###..": ".",
    "..#.#": ".",
    "...##": "#",
    "##...": "#",
    "#####": ".",
    "#.##.": ".",
    ".#..#": "#",
    "##..#": ".",
    ".....": ".",
    "####.": "#",
    "#..##": ".",
    ".##..": "#",
}


def part_one():
    margin = 60
    score0 = 0
    s0 = "".join(("."*margin, STATE0, "."*margin))
    # advance next generation
    for _ in range(50):
        print(s0)
        l1 = ["."] * len(s0)
        for i in range(2, len(s0) - 3):
            nh = s0[i - 2:i + 3]
            g1 = TRANSITIONS[nh]
            l1[i] = g1
        s0 = "".join(l1)
        score1 = score(s0, margin)
        print(score1, score1 - score0)
        score0 = score1  


def score(s0, offset):
    plantscore = 0
    for i in range(len(s0)):
        if s0[i] == "#":
            plantscore += i + offset
    return plantscore


def part_two():
    margin = 4
    offset = -margin
    score0 = 0
    s0 = "".join(("."*margin, STATE0, "."*margin))
    # advance next generation
    for g in range(200):
        res = ["."] * len(s0)
        for i in range(2, len(s0) - 3):
            nh = s0[i - 2:i + 3]
            g1 = TRANSITIONS[nh]
            res[i] = g1
        # trim
        if res[0:3] == list("..#"):
            offset -= 2
            res.insert(0, ".")
            res.insert(0, ".")
        elif res[0:4] == list("...#"):
            offset -= 1
            res.insert(0, ".")
        else:
            while res[0:5] == list("....."):
                offset += 1
                res.pop(0)
        if res[-3:] == list("#.."):
            res.append(".")
            res.append(".")
        elif res[-4:] == list("#..."):
            res.append(".")
        else:
            while res[-5:] == list("....."):
                res.pop(-1)
        s1 = "".join(res)
        score1 = score(s1, offset)
        print(f"{g+1:3} {offset:4} {score1:4} {score1 - score0:4}", s1)
        score0 = score1  
        s0 = s1

"""         
>>> ( 50000000000 - 200 ) * 78 + 17812
3900000002212
"""


if __name__ == '__main__':
    part_two()
