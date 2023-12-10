import re
import math

file = open("6/input.txt", "r")
input = file.readlines()


def part_one(input):
    races = list(
        zip(
            [int(t) for t in re.findall(r"\d+", input[0][9:])],
            [int(t) for t in re.findall(r"\d+", input[1][9:])],
        )
    )

    ways_to_win = []
    for [time, best] in races:
        way = 0
        for i in range(0, time):
            if (time - i) * i > best:
                way += 1

        ways_to_win.append(way)

    return math.prod(ways_to_win)


print(part_one(input))
