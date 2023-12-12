import re

file = open("9/input.txt", "r")
input = file.readlines()


def diff(numbers):
    return [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]


def part_one(input):
    p1 = p2 = 0

    for row in input:
        numbers = [[int(i) for i in row.split()]]

        while len([n for n in numbers[-1] if n != 0]):
            d = diff(numbers[-1])
            numbers.append(d)

        p1v = p2v = 0
        for i in range(len(numbers) - 1, 0, -1):
            p1v = numbers[i][-1] + p1v
            p2v = numbers[i][0] - p2v

        p1 += numbers[0][-1] + p1v
        p2 += numbers[0][0] - p2v

    return [p1, p2]


print("p1: ", part_one(input)[0])
print("p2: ", part_one(input)[1])
