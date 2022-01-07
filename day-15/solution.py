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
from functools import lru_cache


def input(fname):
    lines = open(fname).read().splitlines()
    grid = [list(map(int, list(line))) for line in lines]
    return grid


def part1(fname):

    grid = input(fname)

    m, n = len(grid), len(grid[0])



def part2(fname):

    pass


if __name__ == "__main__":

    day = "15"

    print("part 1 -> test:  ", part1(f"day-{day}/test.txt"))
    print("part 1 -> input: ", part1(f"day-{day}/input.txt"))

    # print("part 2 -> test:  ", part2(f"day-{day}/test.txt"))
    # print("part 2 -> input: ", part2(f"day-{day}/input.txt"))
