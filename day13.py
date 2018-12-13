#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 13 """

import sys
from pathlib import Path

DIRS = {
    "<": (-1, 0),
    ">": (+1, 0),
    "^": (0, -1),
    "v": (0, +1),
}

NEXTTURN = {
    "<": "^",
    "^": ">",
    ">": "<",
}

TURN = {
    "<<": "v",
    "v<": ">",
    "><": "^",
    "^<": "<",
    "<^": "<",
    "v^": "v",
    ">^": ">",
    "^^": "^",
    "<>": "^",
    "v>": "<",
    ">>": "v",
    "^>": ">",
}

MOVE = {
    "<\\": "^",
    "</": "v",
    "<-": "<",
    ">\\": "v",
    ">/": "^",
    ">-": ">",
    "^\\": "<",
    "^/": ">",
    "^|": "^",
    "v\\": ">",
    "v/": "<",
    "v|": "v",
}


class Cart:

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.dir = d
        self.turn = "<"
        self.removed = False

    def move(self, map_):
        dx, dy = DIRS[self.dir]
        x1 = self.x + dx
        y1 = self.y + dy
        newloc = map_[f"{x1},{y1}"]
        if newloc == "+":
            self.dir = TURN[f"{self.dir}{self.turn}"]
            self.turn = NEXTTURN[self.turn]
        else:
            idx = f"{self.dir}{newloc}"
            self.dir = MOVE[idx]
        self.x = x1
        self.y = y1

    def coord(self):
        return (self.x, self.y)


def part_one():
    carts, map_ = load_input()
    # run simulation
    i = 0
    while True:
        print(f"Iteration: {i}, {len(carts)} carts")
        carts.sort(key=lambda c: f"{c.y:03}{c.x:03}")
        for cart in carts:
            cart.move(map_)
            if check_collision(carts):
                sys.exit()
        i += 1


def check_collision(carts):
    points = set()
    for cart in carts:
        coord = (cart.x, cart.y)
        if coord not in points:
            points.add(coord)
        else:
            print(f"Collision at {coord}")
            return coord
    return None


def part_two():
    carts, map_ = load_input()
    # run simulation
    i = 0
    while len(carts) > 1:
        print(f"Iteration: {i}, {len(carts)} carts")
        carts.sort(key=lambda c: f"{c.y:03}{c.x:03}")
        for cart in carts:
            if cart.removed:
                continue
            cart.move(map_)
            for check in carts:
                if cart == check:
                    continue
                if cart.coord() == check.coord():
                    cart.removed = True
                    check.removed = True
        # purge from list
        for cart in list(carts):
            if cart.removed:
                carts.remove(cart)
        i += 1
    print(carts[0].coord())


def load_input():
    carts = []
    map_ = {}
    inp = Path(r"day13_input.txt")
    with inp.open() as fh:
        for y, raw_line in enumerate(fh):
            line = raw_line.rstrip()
            for x, c in enumerate(line):
                if c in "<>^v":
                    cart = Cart(x, y, c)
                    carts.append(cart)
                    if c in "<>":
                        map_[f"{x},{y}"] = "-"
                    elif c in "v^":
                        map_[f"{x},{y}"] = "|"
                    else:
                        raise
                elif c in "-|+/\\":
                    map_[f"{x},{y}"] = c
    return (carts, map_)


if __name__ == '__main__':
    part_two()
