import re

file = open('5/input.txt', 'r')
input = file.readlines()

def parse_input(input):
  seeds = [int(n) for n in input[0][7:].split(' ')]

  maps = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
  }

  key = None
  for row in input[2:]:
    if len(row.strip()) == 0:
      continue

    if 'map' in row:
      key = row.split(' ')[0]
      continue

    values = [int(n) for n in re.findall(r'\d+', row)]
    maps[key].append(values)

  for key, value in maps.items():
    value.sort(key=lambda a : a[1])

  return seeds, maps


def solve(input):
  [seeds, maps] = parse_input(input)

  lowest_value = float('inf')

  for seed in seeds:
    for map in maps.values():
      for [destination, source, range] in map:
        if source <= seed < source + range:
          seed = seed + destination - source
          break

    lowest_value = min(lowest_value, seed)
    
  print(lowest_value)


solve(input)