import re

file = open("9/input.txt", "r")
input = file.readlines()


def diff(numbers):
    return [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]


def part_one(input):
    total = 0

    for row in input:
        numbers = [[int(i) for i in row.split()]]

        while len([n for n in numbers[-1] if n != 0]):
            d = diff(numbers[-1])
            numbers.append(d)

        val = 0
        for i in range(len(numbers) - 1, 0, -1):
            val = numbers[i][-1] + val

        total += numbers[0][-1] + val

    return total


print("p1: ", part_one(input))
# print("p2: ", part_two(input))
