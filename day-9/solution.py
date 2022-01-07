import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, le
from os import error
from pprint import pprint
from collections import deque
import re
from bisect import bisect_left
import math


def input(fname):
    inputString = open(fname).read()
    return [list(map(int, list(line))) for line in inputString.splitlines()]


def part1(fname):
    heightMap = input(fname)
    m, n = len(heightMap), len(heightMap[0])
    return sum(
        heightMap[i][j] + 1
        for i in range(m)
        for j in range(n)
        if all(
            [
                heightMap[i][j] < heightMap[di][dj]
                for di, dj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                if 0 <= di < m and 0 <= dj < n
            ]
        )
    )


def part2(fname):
    heightMap = input(fname)
    basinId = -1
    basinHeights = Counter()

    m, n = len(heightMap), len(heightMap[0])

    def scan(i, j):
        nonlocal heightMap
        if 0 <= i < m and 0 <= j < n and 0 <= heightMap[i][j] < 9:
            heightMap[i][j] = basinId
            basinHeights[basinId] += 1
            for di, dj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                scan(di, dj)

    for i in range(m):
        for j in range(n):
            basinId -= 1
            scan(i, j)

    return math.prod(v for _, v in basinHeights.most_common(3))


if __name__ == "__main__":

    print("part 1 -> test:  ", part1("day-9/test.txt"))
    print("part 1 -> input: ", part1("day-9/input.txt"))

    print("part 2 -> test:  ", part2("day-9/test.txt"))
    print("part 2 -> input: ", part2("day-9/input.txt"))
