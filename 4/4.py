import re

file = open('4/input.txt', 'r')
input = file.readlines()

def get_numbers(number_set):
 return re.findall(r'\d{1,2}', number_set)


def get_matches(row):
  row = row.rstrip()
  [_, numbers] = row.split(': ')
  [my_numbers, winning_numbers] = numbers.split('|')
  my_numbers = get_numbers(my_numbers)
  winning_numbers = get_numbers(winning_numbers)

  def find_matches(target):
    return target in winning_numbers

  return len(list(filter(find_matches, my_numbers)))


def get_winning_cards(index):
  matches = get_matches(input[index])
  winning_cards = []
  
  i = 1
  while i <= matches:
    winning_cards.append(get_winning_cards(index + i))
    i += 1

  return winning_cards


def flatten(array):
    if array == []:
        return 1
    if isinstance(array[0], list):
        return flatten(array[0]) + flatten(array[1:])
    return array[:1] + flatten(array[1:])


def solve(input):
  score = 0
  cards = []

  for index, row in enumerate(input):
    matches = get_matches(row)
    score += 2 ** (matches - 1) if matches > 0 else 0

    cards.append(get_winning_cards(index))

  return score, flatten(cards) - 1


print(solve(input))