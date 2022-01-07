import itertools
from collections import Counter, defaultdict
from itertools import groupby, product
from operator import itemgetter, le
from os import error
from pprint import pprint
from collections import deque
import re
from bisect import bisect_left
import math


def input(fname):
    lines = open(fname).read().splitlines()
    grid = [list(map(int, list(line))) for line in lines]
    return grid


def display(grid):
    print()
    print("\n".join(map(lambda x: "".join(map(str, x)), grid)))
    print()


def neighbours(x, y, restrict, m, n):

    neighbourSet = list(product([x - 1, x + 1, x], [y - 1, y + 1, y]))

    return [
        (dx, dy)
        for dx, dy in neighbourSet
        if 0 <= dx < m
        if 0 <= dy < n
        if (dx, dy) not in restrict
    ]


def part1(fname):

    grid = input(fname)

    m, n = len(grid), len(grid[0])

    res = 0

    for step in range(100):

        flashes = set()

        for i in range(m):
            for j in range(n):
                grid[i][j] += 1
                if grid[i][j] > 9 and (i, j) not in flashes:
                    flashes.add((i, j))
                    stack = neighbours(i, j, flashes, m, n)
                    while stack:
                        (x, y) = stack.pop()
                        grid[x][y] += 1
                        if grid[x][y] > 9 and (x, y) not in flashes:
                            flashes.add((x, y))
                            stack.extend(neighbours(x, y, flashes, m, n))

        res += len(flashes)
        for (i, j) in flashes:
            grid[i][j] = 0

    return res


def part2(fname):

    grid = input(fname)

    m, n = len(grid), len(grid[0])

    res = 0

    for step in range(10 ** 5):

        flashes = set()

        for i in range(m):
            for j in range(n):
                grid[i][j] += 1
                if grid[i][j] > 9 and (i, j) not in flashes:
                    flashes.add((i, j))
                    stack = neighbours(i, j, flashes, m, n)
                    while stack:
                        (x, y) = stack.pop()
                        grid[x][y] += 1
                        if grid[x][y] > 9 and (x, y) not in flashes:
                            flashes.add((x, y))
                            stack.extend(neighbours(x, y, flashes, m, n))

        res += len(flashes)
        for (i, j) in flashes:
            grid[i][j] = 0

        if len(flashes) == m * n:
            return step + 1

    return res


if __name__ == "__main__":

    day = "11"

    print("part 1 -> test:  ", part1(f"day-{day}/test.txt"))
    print("part 1 -> input: ", part1(f"day-{day}/input.txt"))

    print("part 2 -> test:  ", part2(f"day-{day}/test.txt"))
    print("part 2 -> input: ", part2(f"day-{day}/input.txt"))
