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
    return inputString.splitlines()


def part1(fname):

    lines = input(fname)

    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pair = {")": "(", "]": "[", "}": "{", ">": "<"}
    seen = {")": 0, "]": 0, "}": 0, ">": 0}

    for line in lines:
        stack = [line[0]]
        for ch in line[1:]:
            if ch in pair:
                if stack[-1] != pair[ch]:
                    seen[ch] += 1
                    break
                stack.pop()
            else:
                stack.append(ch)

    return sum(freq * score[ch] for ch, freq in seen.items())


def part2(fname):

    lines = input(fname)

    table = str.maketrans({"(": "1", "[": "2", "{": "3", "<": "4"})
    pair = {")": "(", "]": "[", "}": "{", ">": "<"}
    incompletes = []

    for line in lines:
        stack, corrupt = [line[0]], False
        for ch in line[1:]:
            if ch in pair:
                if stack[-1] != pair[ch]:
                    corrupt = True
                    break
                stack.pop()
            else:
                stack.append(ch)
        if not corrupt and stack:
            incompletes.append("".join(stack))

    incompletes = sorted(
        [int(incomplete.translate(table)[::-1], 5) for incomplete in incompletes]
    )
    return incompletes[len(incompletes) // 2]


if __name__ == "__main__":

    day = "10"

    print("part 1 -> test:  ", part1(f"day-{day}/test.txt"))
    print("part 1 -> input: ", part1(f"day-{day}/input.txt"))

    print("part 2 -> test:  ", part2(f"day-{day}/test.txt"))
    print("part 2 -> input: ", part2(f"day-{day}/input.txt"))
