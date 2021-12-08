import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter
import re


def input(fname):

    lines = [line.strip() for line in open(fname).read().splitlines() if line]
    moves = list(map(int, lines[0].split(",")))
    puzzles = []

    for lineno in range(1, len(lines), 5):
        puzzles.append(dict(rows=defaultdict(set), cols=defaultdict(set), nums={}))
        for i in range(5):
            nums = list(map(int, re.split(r"\s+", lines[lineno + i])))
            for j, num in enumerate(nums):
                puzzles[-1]["nums"][num] = (i, j)
                puzzles[-1]["rows"][i].add(num)
                puzzles[-1]["cols"][j].add(num)

    return moves, puzzles


def part1(fname):
    moves, puzzles = input(fname)
    for move in moves:
        for puzzle in puzzles:
            if move in puzzle["nums"]:
                row, col = puzzle["nums"][move]
                puzzle["rows"][row].remove(move)
                puzzle["cols"][col].remove(move)
                if len(puzzle["rows"][row]) == 0:
                    return sum(sum(v) for _, v in puzzle["rows"].items()) * move
                if len(puzzle["cols"][col]) == 0:
                    return sum(sum(v) for _, v in puzzle["cols"].items()) * move


def part2(fname):
    moves, puzzles = input(fname)
    wonSet = set()
    for move in moves:
        for idx, puzzle in enumerate(puzzles):
            if move in puzzle["nums"]:
                row, col = puzzle["nums"][move]
                puzzle["rows"][row].remove(move)
                puzzle["cols"][col].remove(move)

                if len(puzzle["rows"][row]) == 0:
                    wonSet.add(idx)
                    if len(wonSet) == len(puzzles):
                        return sum(sum(v) for _, v in puzzle["rows"].items()) * move
                if len(puzzle["cols"][col]) == 0:
                    wonSet.add(idx)
                    if len(wonSet) == len(puzzles):
                        return sum(sum(v) for _, v in puzzle["cols"].items()) * move


if __name__ == "__main__":

    print("part 1 -> test:  ", part1("day-4/test.txt"))
    print("part 1 -> input: ", part1("day-4/input.txt"))

    print("part 2 -> test:  ", part2("day-4/test.txt"))
    print("part 2 -> input: ", part2("day-4/input.txt"))
