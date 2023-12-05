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


def follow_map(seed, maps):
  for map in maps.values():
    for [destination, source, range] in map:
      if source <= seed < source + range:
        seed = seed + destination - source
        break
  
  return seed

def reverse_map(maybe, maps):
  for map in reversed(list(maps.values())):
    for [destination, source, range] in map:
      if destination <= maybe < destination + range:
        maybe = maybe + source - destination
        break
        
        
  return maybe


def part_one(input):
  [seeds, maps] = parse_input(input)

  lowest_value = float('inf')

  for seed in seeds:
    lowest_value = min(lowest_value, follow_map(seed, maps))
    
  return lowest_value


def part_two(input):
  [seeds, maps] = parse_input(input)

  max_value = max(seeds[i] + seeds[i + 1] for i in range(0, len(seeds), 2))
  
  for i in range(max_value):
    seed = reverse_map(i, maps)

    if seed in seeds:
      return seed
    
  return None

print('Part 1:', part_one(input))
print('Part 2:', part_two(input))