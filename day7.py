#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 7 """

from pathlib import Path
from collections import defaultdict
import heapq


def part_one():
    inp = Path(r"day7_input.txt")
    prereqs = defaultdict(list)
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            tokens = line.split(" ")
            action = tokens[7]
            prereq = tokens[1]
            prereqs[action].append(prereq)
            # add starting point(s)
            if prereq not in prereqs:
                prereqs[prereq] = list()
    while len(prereqs) > 0:
        available = list()
        for k, v in prereqs.items():
            if len(v) == 0:
                available.append(k)
        available.sort()
        # start with smallest char
        action = available[0]
        print(action, end="")
        del prereqs[action]
        for k, v in prereqs.items():
            if action in v:
                v.remove(action)


def part_two():
    inp = Path(r"day7_input.txt")
    prereqs = defaultdict(list)
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            tokens = line.split(" ")
            action = tokens[7]
            prereq = tokens[1]
            prereqs[action].append(prereq)
            # add starting point(s)
            if prereq not in prereqs:
                prereqs[prereq] = list()
    h = []
    heapq.heapify(h)
    t = 0
    actions = ""
    workers = 5
    while len(prereqs) > 0 or len(h) > 0:
        # finish available step
        if len(h) > 0:
            t1, action = heapq.heappop(h)
            t = t1
            # complete action - remove prereqs
            actions += action
            for k, v in prereqs.items():
                if action in v:
                    v.remove(action)
        # find available steps
        available = list()
        for k, v in prereqs.items():
            if len(v) == 0:
                available.append(k)
        available.sort()
        # queue available steps
        while len(h) <= workers:
            if not len(available):
                break
            action = available.pop(0)
            del prereqs[action]
            heapq.heappush(h, (t + duration(action), action))
        heaps = ""
        for n in range(workers):
            if len(h) > n:
                heaps += f"{h[n][0]:4}/{h[n][1]}"
            else:
                heaps += "     ."
        print(f"{t:4} {heaps} {actions}")


def duration(c):
    d = 61 + ord(c) - ord("A")
    return d


if __name__ == '__main__':
    part_two()
