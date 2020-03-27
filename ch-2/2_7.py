# Exercise 2-7. Stripping Names: Use a variable to represent a person’s
# name, and include some whitespace characters at the beginning and end of
# the name. Make sure you use each character combination, "\t" and "\n",
# at least once. Print the name once, so the whitespace around the name is
# displayed. Then print the name using each of the three stripping
# functions, lstrip(), rstrip(), and strip().
#
cool_name = " Cool Name "

print(f"Usting strip functions on name: {cool_name}")
print("lstrip()")
print(cool_name.lstrip())

print("rstrip()")
print(cool_name.rstrip())

print("strip()")
print(cool_name.strip())
