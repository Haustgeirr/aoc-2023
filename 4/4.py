import re

file = open('4/input.txt', 'r')
input = file.readlines()

def get_numbers(number_set):
 return re.findall(r'\d{1,2}', number_set)

def part_one(input):
  score = 0

  for row in input:
    row = row.rstrip()
    [_, numbers] = row.split(': ')
    [my_numbers, winning_numbers] = numbers.split('|')
    my_numbers = get_numbers(my_numbers)
    winning_numbers = get_numbers(winning_numbers)

    def find_matches(target):
      return target in winning_numbers

    matches = list(filter(find_matches, my_numbers))
    score += 2 ** (len(matches) - 1) if len(matches) > 0 else 0

  return score


print(part_one(input))