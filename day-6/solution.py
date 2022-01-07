import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, le
from os import error
from pprint import pprint
import re


def input(fname):
    clocks = list(map(int, open(fname).read().strip().split(",")))
    return clocks


def part1(fname, days=80):

    clocks = input(fname)

    dp = [[0] * 9 for _ in range(days + 1)]

    for clock in clocks:
        dp[0][clock] += 1

    for day in range(1, days + 1):
        dp[day][6] = dp[day][8] = dp[day - 1][0]
        for clock in range(8):
            dp[day][clock] += dp[day - 1][clock + 1]

    return sum(dp[-1])


def part2(fname):
    return part1(fname=fname, days=256)


if __name__ == "__main__":

    print("part 1 -> test:  ", part1("day-6/test.txt"))
    print("part 1 -> input: ", part1("day-6/input.txt"))

    print("part 2 -> test:  ", part2("day-6/test.txt"))
    # print("part 2 -> input: ", part2("day-6/input.txt"))
