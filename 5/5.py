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

# Next is to handle how we split
# which bucket does a number fall into
# its in the example
# then finish the permutes
# then iterate through the seed_ranges
# finall iterate the seed_ranges through the map
# then fin?!
def split_range(range, ranges):
  new_ranges = [range]
  index = 0
  [s0, s1] = new_ranges[index]
  for [d0, d1, delta] in ranges:
    print(range, [d0, d1])
    if s0 < s1 < d0 < d1:
      print('no overlap, s lower')
      break
    
    if d0 < d1 < s0 < s1:
      print('no overlap, d lower')
      continue

    if s0 < d0 < s1 < d1:
      print('overlap, s left')
      new_ranges[index] = [s0, d0]
      new_ranges.append([d0, s1])
      new_ranges.append([s1, d1])
      index += 1
      continue

    if d0 < s0 < d1 < s1:
      print('overlap, d left')

    if s0 < d0 < d1 < s1:
      print('s encloses d')

    if d0 < s0 < s1 < d1:
      print('d encloses s')
      new_ranges[index] = [d0, s0]
      new_ranges.append([s0, s1])
      new_ranges.append([s1, d1])
      index += 1
      break

  print(new_ranges)


def part_two(input):
  [seeds, maps] = parse_input(input)
  seed_ranges = [[seeds[i],  seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]
  step_ranges = [[r[1], r[1] + r[2], r[0] - r[1]] for r in list(maps.values())[0]]
  ranges = split_range(seed_ranges[0], step_ranges)

# print('Part 1:', part_one(input))
print('Part 2:', part_two(input))