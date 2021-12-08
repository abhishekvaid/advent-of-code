import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, le
from os import error
import re


def input(fname):
    """
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2

    partition points into two sets:
        horizontal lines:
        vertical lines:

    parition each set into lines / cols:
        horizontal ->
            line 0 ->
            line 1 ->
            line 2 -> (1, 4), (2, 5), (4, 10)  --> (2, 2), (2, 3), (2, 4)

    """

    lines = []
    for inputLine in open(fname).read().splitlines():
        left, right = inputLine.split(" -> ")
        leftPoint, rightPoint = list(int, left.split(",")), list(int, right.split(","))
        lines.append([leftPoint, rightPoint])

    return lines


def part1(fname):
    
    lines = input()
    lines.sort(key=lambda x: (x[0][0], x[0][1]))
    horizontalLines = defaultdict(lambda: dict(segments=defaultdict(list), res=set()))
    verticalLines = defaultdict(lambda: dict(segments=defaultdict(list), res=set()))
    
    for line in lines:
        [[leftX, leftY], [rightX, rightY]] = line
        if leftX == rightX:
            horizontalLines[leftX]["segments"].append((leftY, rightY))
        elif leftY == rightY:
            verticalLines[leftY]["segments"].append((leftX, rightX))
        else:
            raise error("Impossible")
        
    for k, v in horizontalLines.items():
        for ([y1, y2], [y3, y4]) in zip(v[:-1], v[1:]):
            
            


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
