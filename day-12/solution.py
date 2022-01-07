import itertools
from collections import Counter, defaultdict
from itertools import groupby, product
from operator import itemgetter, le
from os import error, kill
from pprint import pprint
from collections import deque
import re
from bisect import bisect_left
import math


def input(fname):
    Graph = defaultdict(list)
    for line in open(fname).read().splitlines():
        x, y = line.split("-")
        Graph[x].append(y)
        Graph[y].append(x)
    return Graph


def part1(fname):
    Graph = input(fname)
    paths = []
    stack = [("start", ["start"], {"start"})]
    while stack:
        cur, path, visited = stack.pop()
        for neighbour in Graph[cur]:
            if neighbour == "end":
                paths.append(list(path) + ["end"])
            else:
                if neighbour.isupper():
                    stack.append((neighbour, path + [neighbour], visited))
                else:
                    if neighbour not in visited:
                        stack.append(
                            (neighbour, path + [neighbour], visited | {neighbour})
                        )

    return len(paths)


def part2(fname):

    Graph = input(fname)
    paths, visited = [], {1: set(), 2: set()}
    stack = [("start", ["start"], visited)]
    visited[1].add("start")
    while stack:
        cur, path, visited = stack.pop()
        for neighbour in Graph[cur]:
            if neighbour == "end":
                paths.append(list(path) + ["end"])
            elif neighbour == "start":
                continue
            else:
                if neighbour not in visited[1]:
                    visited_ = dict(visited)
                    visited_[1].add(neighbour)
                    stack.append((neighbour, path + [neighbour], visited_))
                else:
                    if len(visited[2]) == 0:
                        visited_ = dict(visited)
                        visited_[2].add(neighbour)
                        stack.append((neighbour, path + [neighbour], visited_))
                        stack.append((neighbour, path + [neighbour], visited))

    # pprint(list(map(tuple, paths)))

    """
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
    """

    print("\n".join(sorted(",".join(path) for path in paths)))

    return len(paths)


if __name__ == "__main__":

    day = "12"

    # print("part 1 -> test:  ", part1(f"day-{day}/test.txt"))
    # print("part 1 -> test:  ", part1(f"day-{day}/test2.txt"))
    # print("part 1 -> test:  ", part1(f"day-{day}/test3.txt"))
    # print("part 1 -> input: ", part1(f"day-{day}/input.txt"))

    print("part 2 -> test:  ", part2(f"day-{day}/test.txt"))
    # print("part 2 -> test:  ", part2(f"day-{day}/test.txt"))
    # print("part 2 -> input: ", part2(f"day-{day}/input.txt"))
