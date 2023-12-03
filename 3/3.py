import re
from functools import reduce

input = open('3/input.txt', 'r').readlines()

def get_span(match):
  return match.start()

def get_symbol_rows(index):
  rows = []
  if index != 0:
    rows = rows + list(map(get_span, re.finditer(r'[^.\n\d]', input[index - 1])))
    
  rows = rows + list(map(get_span, re.finditer(r'[^.\n\d]', input[index])))

  if index < len(input) - 1:
    rows = rows + list(map(get_span, re.finditer(r'[^.\n\d]', input[index + 1])))

  return rows

def part_one(input):
  part_number_total = 0

  for i, row in enumerate(input):
    symbol_check_rows = get_symbol_rows(i)

    def compare_symbols(number):
      valid = False
      for s in symbol_check_rows:
        if number.start() - 1 <= s <= number.end():
          valid = True
      
      return valid

    numbers = list(filter(compare_symbols, re.finditer(r'\d+', row)))
    for n in numbers:
      part_number_total += int(n.group())

  return part_number_total

print(part_one(input))