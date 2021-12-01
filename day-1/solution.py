entries = list(map(int, open("input.txt").read().split("\n")))


def part1():
    print("part1: ", sum(1 if y > x else 0 for x, y in zip(entries[:-1], entries[1:])))


def part2():
    print("part2: ", sum(1 if y > x else 0 for x, y in zip(entries[:-1], entries[3:])))



if __name__ == "__main__":
    part1()
    part2()
