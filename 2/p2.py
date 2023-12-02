file = open('2/input.txt', 'r')
input = file.readlines()

max_cubes = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def solve(input):
  game_values = []

  for row in input:
    min_cubes = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    row = row.rstrip()
    [_, hands] = row.split(': ')
    hands = hands.split('; ')
    
    for hand in hands:
      combinations = hand.split(', ')
      for cubes in combinations:
        [count, colour] = cubes.split(' ')

        if int(count) > min_cubes[colour]:
          min_cubes.update({ colour : int(count) })

    [r, g, b] = min_cubes.values()
    game_values.append(r * g * b)

  return sum(game_values)


print(solve(input))