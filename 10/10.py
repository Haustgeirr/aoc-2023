import numpy as np

input = open("10/input.txt", "r").readlines()

tiles = {
    "|": [[-1, 0], [1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
}

start_check = {
    "up": {"dir": [-1, 0], "valid": ["|", "7", "F"]},
    "right": {"dir": [0, 1], "valid": ["-", "7", "J"]},
    "down": {"dir": [1, 0], "valid": ["|", "L", "J"]},
    "left": {"dir": [0, -1], "valid": ["-", "L", "F"]},
}

grid = np.array([list(row.strip()) for row in input])


def invert(dir):
    return [dir[0] * -1, dir[1] * -1]


def diff(a, b):
    return [a[0] - b[0], a[1] - b[1]]


def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def get_tile(dir):
    return grid[dir[0]][dir[1]]


def part_one():
    start = [
        [ix, iy] for ix, row in enumerate(grid) for iy, i in enumerate(row) if i == "S"
    ][0]

    # get first two dirs
    print("start", start)
    prev = start
    loc = start
    dir = None
    for val in start_check.values():
        dir = val["dir"]
        valid = val["valid"]
        adj = [start[0] + dir[0], start[1] + dir[1]]
        tile = get_tile(adj)

        if tile in valid:
            loc = adj
            break

    steps = 0
    while loc != start:
        dir = diff(loc, prev)
        tile = get_tile(loc)
        prev = loc

        if invert(dir) == tiles[tile][0]:
            loc = add(loc, tiles[tile][1])
        else:
            loc = add(loc, tiles[tile][0])

        steps += 1

    return (steps + 1) / 2


print("1: ", part_one())
