file = open('1/input2.txt', 'r')
input = file.readlines()

def solve(input):
  values = []
  numbersDict = [
    ('zero', '0'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven',  '7'),
    ('eight', '8'),
    ('nine', '9')
  ]

  for row in input:
    i = 0
    first = None
    last = None

    while i <= len(row):
      if first == None:
        if row[i].isdigit():
          first = row[i]
        
        for number in numbersDict:
          if (number[0] in row[0:i]):
            first = number[1]

      if last == None:
        if row[len(row) - 1 - i].isdigit():
          last = row[len(row) - 1 - i]
        
        for number in numbersDict:
          if (number[0] in row[len(row) - 1 - i:len(row)]):
            last = number[1]

      if (first != None and last != None):
        values.append(int(first + last))
        break

      i += 1

  return sum(values)

print(solve(input))