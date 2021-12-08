import itertools
from collections import Counter, defaultdict


def input():
    D = defaultdict(int)
    for line in open("input.txt").read().splitlines():
        move, value = line.split(" ")
        D[move] += int(value)
    return D


def part1():
    D = input()
    return D["forward"] * (D["down"] - D["up"])


def part2():
    aim, horizontal, depth = 0, 0, 0
    for line in open("input.txt").read().splitlines():
        move, value = line.split(" ")
        value = int(value)
        if move == "forward":
            horizontal += value
            depth += aim * value
        elif move == "down":
            aim += value
        else:
            aim -= value
    return horizontal * depth


if __name__ == "__main__":
    print(part1())
    print(part2())
