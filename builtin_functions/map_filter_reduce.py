from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map(): apply a function to every item
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

# filter(): keep items that match a condition
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce(): combine items into one value
total = reduce(lambda first, second: first + second, numbers)
product = reduce(lambda first, second: first * second, numbers)
print("Sum with reduce:", total)
print("Product with reduce:", product)

# Other useful built-in functions
print("len:", len(numbers))
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sorted descending:", sorted(numbers, reverse=True))

# Type checking and conversions
value = "25"
print("type:", type(value))
integer_value = int(value)
float_value = float(value)
string_value = str(integer_value)
print("int:", integer_value, type(integer_value))
print("float:", float_value, type(float_value))
print("str:", string_value, type(string_value))
print("bool conversion of non-empty string:", bool("hello"))
