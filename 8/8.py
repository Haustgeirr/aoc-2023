import re
import math

file = open("8/input.txt", "r")
input = file.readlines()


def parse(input):
    route = input[0].strip()
    nodes = {
        key: (left, right)
        for [key, left, right] in (re.findall(r"\w{3}", row) for row in input[2:])
    }

    return [route, nodes]


def part_one(input):
    [route, nodes] = parse(input)

    key = "AAA"
    steps = 0
    while key != "ZZZ":
        dir = route[steps % len(route)]
        key = nodes[key][0] if dir == "L" else nodes[key][1]
        steps += 1

    return steps


def part_two(input):
    [route, nodes] = parse(input)
    starting_keys = [key for key in nodes.keys() if re.match(r".{2}A", key)]

    keys = starting_keys.copy()
    factors = []
    for k in keys:
        key = k
        steps = 0
        while not re.match(r".{2}Z", key) and steps < 30000:
            dir = route[steps % len(route)]
            key = nodes[key][0] if dir == "L" else nodes[key][1]
            steps += 1

        factors.append(steps)

    return math.lcm(*factors)


print("p1: ", part_one(input))
print("p2: ", part_two(input))
