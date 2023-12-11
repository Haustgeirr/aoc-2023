import re

file = open("8/input.txt", "r")
input = file.readlines()


def part_one(input):
    route = input[0].strip()
    nodes = {
        key: (left, right)
        for [key, left, right] in (re.findall(r"\w{3}", row) for row in input[2:])
    }

    key = "AAA"
    steps = 0
    while key != "ZZZ":
        dir = route[steps % len(route)]
        key = nodes[key][0] if dir == "L" else nodes[key][1]
        steps += 1

    return steps


print("p1: ", part_one(input))
