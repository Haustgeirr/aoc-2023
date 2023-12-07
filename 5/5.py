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


def split_range(range, ranges):
  new_ranges = [range]
  index = 0
  [s0, s1] = new_ranges[index]
  for [d0, d1, delta] in ranges:
    # no overlap, s lower
    if s0 < s1 < d0 < d1:
      break
    
    # no overlap, d lower
    if d0 < d1 < s0 < s1:
      continue

    # overlap, perfect
    if s0 == d0  and s1 == d1:
      new_ranges[index] = [s0 + delta, s1 + delta]
      break

    # overlap, s left
    if s0 < d0 <= s1 <= d1:
      new_ranges[index] = [s0, d0 - 1]
      new_ranges.append([d0 + delta, s1 + delta])
      index += 1
      continue

    # overlap, d left
    if d0 < s0 <= d1 <= s1:
      new_ranges[index] = [s0 + delta, d1 + delta]
      if (d1 < s1):
        new_ranges.append([d1 + 1, s1])
      index += 1
      continue

    # s encloses d
    if s0 < d0 < d1 < s1:
      new_ranges[index] = [s0, d0 - 1]
      new_ranges.append([d0 + delta, d1 + delta])
      new_ranges.append([d1 + 1, s1])
      index += 1
      break

    # d encloses s
    if d0 < s0 < s1 < d1:
      new_ranges[index] = [s0 + delta, s1 + delta]
      index += 1
      break

  return new_ranges


def recursive_merge(inter, start_index = 0):
  for i in range(start_index, len(inter) - 1):
      if inter[i][1] > inter[i+1][0]:
          new_start = inter[i][0]
          new_end = inter[i+1][1]
          inter[i] = [new_start, new_end]
          del inter[i+1]
          return recursive_merge(inter.copy(), start_index=i)
  return inter    


def part_two(input):
  [seeds, maps] = parse_input(input)
  seed_ranges = [[seeds[i],  seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]
  step_ranges = [[[r[1], r[1] + r[2] - 1, r[0] - r[1]] for r in maps] for maps in list(maps.values())]

  input_ranges = seed_ranges
  output_ranges = []
  for step in step_ranges:
    output_ranges = []
    for input in input_ranges:
      output_ranges += split_range(input, step)
    
    output_ranges.sort(key=lambda a: (a[0], a[1]))
    merged = recursive_merge(output_ranges.copy())
    input_ranges = merged

  output_ranges.sort(key=lambda a: (a[0], a[1]))
  return output_ranges[0][0]
  

print('Part 1:', part_one(input))
print('Part 2:', part_two(input))

# print(split_range([10, 20], [[10, 20, 100]])) # overlap, perfect
# print(split_range([10, 20], [[15, 20, 100]]))
# print(split_range([10, 20], [[15, 25, 100]]))
# print(split_range([10, 20], [[20, 30, 100]]))
# print(split_range([10, 20], [[0, 10, 100]]))
# print(split_range([10, 20], [[5, 15, 100]]))  
# print(split_range([10, 20], [[5, 10, 100]]))  
# print(split_range([10, 20], [[5, 25, 100]]))
# print(split_range([10, 20], [[11, 19, 100]]))