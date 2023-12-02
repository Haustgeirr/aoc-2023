file = open('2/input.txt', 'r')
input = file.readlines()

max_cubes = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def solve(input):
  valid_games = []

  for row in input:
    row = row.rstrip()
    [game_detail, hands] = row.split(': ')
    game_id = int(game_detail.split(' ')[-1])
    hands = hands.split('; ')
    
    valid_hands = True
    for hand in hands:
      combinations = hand.split(', ')
      for cubes in combinations:
        [count, colour] = cubes.split(' ')

        if int(count) > max_cubes[colour]:
          valid_hands = False

    if valid_hands:
      valid_games.append(game_id)

  return sum(valid_games)


print(solve(input))