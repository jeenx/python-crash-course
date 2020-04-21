# Exercise 4-9. Cube Comprehension: Use a list comprehension to generate a list
# of the first 10 cubes.

num_list = list(range(1, 11))

cubes = [num ** 3 for num in num_list]
print(cubes)
