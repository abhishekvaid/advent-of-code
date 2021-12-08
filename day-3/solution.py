import itertools
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter


def input(fname):
    nums = open(fname).read().splitlines()
    numBits = len(nums[0])
    return nums, numBits


def part1(fname):
    gamma = epsilon = 0
    nums, numBits = input(fname)
    for idx in range(numBits):
        ones, zeros = 0, 0
        for num in nums:
            if num[idx] == "1":
                ones += 1
            else:
                zeros += 1
        gamma = gamma * 2 + (ones >= zeros)
        epsilon = epsilon * 2 + ((zeros >= ones))
    return epsilon * gamma


def part2(fname):
    def reducePartition(elems, operator, pred):
        partitions = [list(vals) for _, vals in groupby(elems, operator)]
        sorted(partitions, key=lambda x: (len(x), x["1"]), reverse=True)

    nums, numBits = input(fname)
    oxygen, co2, bitIdx = list(nums), nums, 0
    for bitIdx in range(numBits):
        if len(oxygen) > 1:
            partitions = [[], []]
            for num in oxygen:
                partitions[num[bitIdx] == "1"].append(num)
            partitions.sort(
                key=lambda x: (len(x), x[0][bitIdx] == "1" if x else 0), reverse=True
            )
            oxygen = partitions[0]

        if len(co2) > 1:
            partitions = [[], []]
            for num in co2:
                partitions[num[bitIdx] == "1"].append(num)
            partitions.sort(key=lambda x: (len(x), x[0][bitIdx] == "1" if x else 0))
            co2 = partitions[0]

        if len(oxygen) == len(co2) == 1:
            break

    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    print(part1("day-3/input.txt"))
    print(part2("day-3/input.txt"))
