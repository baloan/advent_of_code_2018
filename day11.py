#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 11 """

from functools import lru_cache


def part_one(size=3):
    cells = []
    for y0 in range(1, 301 - size):
        for x0 in range(1, 301 - size):
            f3x3 = 0
            for y in range(y0, y0 + size):
                for x in range(x0, x0 + size):
                    f3x3 += power_level(x, y)
                    # print(f"{power_level(x, y, 18):3}", end="")
                # print()
            cells.append((f"{x0},{y0}", f3x3))
    t = max(cells, key=lambda x: x[1])
    return (t[0], t[1], size)


def part_two():
    for i in range(3, 30):
        print(part_one(i))


@lru_cache(maxsize=90000)
def power_level(x, y, grid=7165):
    """ x (1,300), y (1,300) """
    rack_id = x + 10
    a = rack_id * y
    b = a + grid
    c = b * rack_id
    digit = int(str(c)[-3]) if c > 100 else 0
    power = digit - 5
    return power


if __name__ == '__main__':
    part_two()
