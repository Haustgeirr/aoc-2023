import re

input = open('3/input.txt', 'r').readlines()

def get_for_star(match):
  return match.start(), match.end(), int(match.group())

def get_for_symbol(match):
  return match.start()

def get_adj_rows(index, regex, getter):
  rows = []
  if index != 0:
    rows = rows + list(map(getter, re.finditer(regex, input[index - 1])))
    
  rows = rows + list(map(getter, re.finditer(regex, input[index])))

  if index < len(input) - 1:
    rows = rows + list(map(getter, re.finditer(regex, input[index + 1])))

  return rows

def part_one(input):
  part_number_total = 0

  for i, row in enumerate(input):
    symbol_check_rows = get_adj_rows(i, r'[^.\n\d]', get_for_symbol)

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

def part_two(input):
  gear_ratio_total = 0
  for i, row in enumerate(input):
    adj_rows = get_adj_rows(i, r'\d+', get_for_star)

    def compare_symbols(star):
      ratios = []
      # check for overlapping numbers and increment count every time we find one with exactly two overlaps
      for number in adj_rows:
        star_pos = star.start()
        
        if number[0] - 1 <= star_pos <= number[1]:
          ratios.append(number[2])

      if len(ratios) == 2:
        return ratios[0] * ratios[1]
      
      return 0

    gears = list(map(compare_symbols, re.finditer(r'\*', row)))
    gear_ratio_total += sum(gears)
    

  return gear_ratio_total

print(part_one(input))
print(part_two(input))