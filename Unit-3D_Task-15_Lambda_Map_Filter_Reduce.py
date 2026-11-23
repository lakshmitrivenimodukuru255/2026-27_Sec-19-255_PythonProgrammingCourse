from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
total_sum = reduce(lambda acc, x: acc + x, numbers)

print("Squared (map):", squared)
print("Even numbers (filter):", even_numbers)
print("Sum (reduce):", total_sum)
