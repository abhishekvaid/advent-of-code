import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, le
from os import error
from pprint import pprint
from collections import deque
import re
from bisect import bisect_left


def input(fname):
    positions = list(map(int, open(fname).read().strip().split(",")))
    return positions


def part1(fname):
    """[1, 3, 7 ]
        [

        leftCount ->
        rightCount ->
            (1, 2, 3, 1, 1,  1,  1)
            (0, 1, 2, 4, 7, 14, 16),
    m - 2 + 1 -
        ]
        788
    """

    positions, freqs = list(zip(*sorted(Counter(input(fname)).items())))
    leftCount, rightCount = [], deque()

    for i in range(len(positions)):
        if i == 0:
            leftCount.append(0)
            rightCount.appendleft(0)
        else:
            leftCount.append(freqs[i - 1] + leftCount[-1])
            rightCount.appendleft(freqs[-i] + rightCount[0])

    distanceAccumulator = [
        sum([(positions[i] - positions[0]) * freqs[i] for i in range(len(positions))])
    ]

    for i in range(len(positions) - 1):
        distanceAccumulator.append(
            distanceAccumulator[i]
            + rightCount[i] * (positions[i] - positions[i + 1])
            + leftCount[i + 1] * (positions[i + 1] - positions[i]),
        )

    return min(distanceAccumulator)


def part2(fname):

    positions, freqs = list(zip(*sorted(Counter(input(fname)).items())))

    def squaredDist(n):
        return abs(n * (n + 1) // 2)

    distanceAccumulator = []

    for i in range(max(positions)):

        distanceAccumulator.append(
            sum(
                squaredDist(abs(positions[j] - i)) * freqs[j]
                for j in range(len(positions))
            )
        )

    return min(distanceAccumulator)


if __name__ == "__main__":

    print("part 1 -> test:  ", part1("day-7/test.txt"))
    print("part 1 -> input: ", part1("day-7/input.txt"))

    print("part 2 -> test:  ", part2("day-7/test.txt"))
    print("part 2 -> input: ", part2("day-7/input.txt"))
