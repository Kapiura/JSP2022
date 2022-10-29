from itertools import chain

numbers = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

print(numbers)

numbers = list(chain(numbers[0],numbers[1], numbers[2], numbers[3]))

print(numbers)