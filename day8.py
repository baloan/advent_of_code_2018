#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 8 """

from collections import defaultdict
from pathlib import Path
from pprint import pprint

NODES = []


def part_one():
    inp = Path(r"day8_input.txt")
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            s_tokens = line.split(" ")
            tokens = [int(t) for t in s_tokens]
    parse(tok_iter(tokens))
    meta_sum = 0
    for node in NODES:
        metas = node[1]
        for meta in metas:
            meta_sum += meta
    print(meta_sum)
    # pprint(NODES)


def tok_iter(tokens):
    for tok in tokens:
        yield tok


def parse(ti):
    global NODES
    child_count = next(ti)
    meta_count = next(ti)
    children = [parse(ti) for _ in range(child_count)]
    metas = [next(ti) for _ in range(meta_count)]
    node = (children, metas)
    NODES.append(node)
    return node


def part_two():
    inp = Path(r"day8_input.txt")
    with inp.open() as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            s_tokens = line.split(" ")
            tokens = [int(t) for t in s_tokens]
    root_node = parse(tok_iter(tokens))
    n = von(root_node)
    print(n)


def von(node):
    """ value of nodes """
    children, metas = node
    if len(children) > 0:
        val = 0
        # print(len(children), metas)
        for n, child in enumerate(children):
            factor = 0 
            for meta in metas:
                if meta == n + 1:
                    factor += 1
            # print(f"{n}: {factor}")
            if factor > 0:
                val += von(child) * factor
    else:
        val = sum(metas) if len(metas) > 0 else 0
    return val

if __name__ == '__main__':
    part_two()
