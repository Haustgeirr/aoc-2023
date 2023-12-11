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
    steps = 0
    factors = []
    while len(keys) > 0:
        dir = route[steps % len(route)]
        steps += 1

        for i, key in enumerate(keys):
            new_key = nodes[key][0] if dir == "L" else nodes[key][1]

            if re.match(r".{2}Z", new_key):
                keys.pop(i)
                factors.append(steps)
            else:
                keys[i] = new_key

    return math.lcm(*factors)


print("p1: ", part_one(input))
print("p2: ", part_two(input))
