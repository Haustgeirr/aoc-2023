import re

file = open("5/input.txt", "r")
input = file.readlines()


def parse_input(input):
    seeds = [int(n) for n in input[0][7:].split(" ")]

    maps = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    key = None
    for row in input[2:]:
        if len(row.strip()) == 0:
            continue

        if "map" in row:
            key = row.split(" ")[0]
            continue

        values = [int(n) for n in re.findall(r"\d+", row)]
        maps[key].append(values)

    for key, value in maps.items():
        value.sort(key=lambda a: a[1])

    return seeds, maps


def follow_map(seed, maps):
    for map in maps.values():
        for [destination, source, range] in map:
            if source <= seed < source + range:
                seed = seed + destination - source
                break

    return seed


def part_one(input):
    [seeds, maps] = parse_input(input)

    lowest_value = float("inf")

    for seed in seeds:
        lowest_value = min(lowest_value, follow_map(seed, maps))

    return lowest_value


def split_range(range, splitter):
    [s0, s1] = range
    [d0, d1, delta] = splitter

    d0_norm = d0 - s0  # negative means d0 is on left

    output_ranges = []
    rem = False

    if d0_norm > 0 and s1 > d0_norm:
        output_ranges = [[s0, d0_norm], [d0 + delta, min(s1 - d0_norm, d1)]]

        rem_range = s1 - d0_norm - min(s1, d1)

        if rem_range > 0:
            output_ranges.append([s0 + s1 - rem_range, rem_range])
            rem = True

    elif d0_norm + d1 > 0:
        output_ranges = [[s0 + delta, min(s1, d1 + d0_norm)]]
        rem_range = s1 - min(s1, d1 + d0_norm)

        if rem_range > 0:
            output_ranges.append([s0 + s1 - rem_range, rem_range])
            rem = True
    elif s0 == d0 and s1 == d1:
        output_ranges = [[s0 + delta, s1]]
    else:
        output_ranges = [range]
        rem = True

    return [output_ranges, rem]


def split_ranges(seed, ranges):
    new_ranges = []
    for index, range in enumerate(ranges):
        [out, hasRem] = split_range(seed, range)

        if hasRem:
            new_ranges += out[:-1]
            seed = out[-1]
            if index == len(ranges) - 1:
                new_ranges += [seed]
        else:
            new_ranges += out
            break

    return new_ranges


def part_two(input):
    [seeds, maps] = parse_input(input)
    seeds = [[s[0], s[1]] for s in zip(seeds[::2], seeds[1::2])]
    steps = [[[r[1], r[2], r[0] - r[1]] for r in maps] for maps in list(maps.values())]

    current_seeds = seeds
    for step in steps:
        working_seeds = []
        for seed in current_seeds:
            working_seeds += split_ranges(seed, step)

        current_seeds = working_seeds

    return min(list(map(lambda x: x[0], current_seeds)))


print(part_one(input))
print(part_two(input))
