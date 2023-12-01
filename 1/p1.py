file = open('1/input1.txt', 'r')
input = file.readlines()

def solve(input):
  values = []

  for row in input:
    i = 0
    first = None
    last = None

    while i < len(row):
      if (first == None and row[i].isdigit()):
        first = row[i]

      if (last == None and row[len(row)-1-i].isdigit()):
        last = row[len(row)-1-i]

      if (first != None and last != None):
        values.append(int(first + last))
        break

      i += 1

  return sum(values)


print(solve(input))