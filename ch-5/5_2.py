# Exercise 5-2. More Conditional Tests: You don’t have to limit the number of
# tests you create to ten. If you want to try more comparisons, write more
# tests and add them to conditional_tests.py. Have at least one True and one
# False result for each of the following:
"""
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less 
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
# 1 - Testing for equality and inequality
car = "toyota"
print("Is car == 'toyota'? I predict True.")
print(car == "toyota")

print("\nIs car != 'audi'? I predict True.")
print(car != "audi")
# 2 Testing using lower() method
name = "Jim"
l_name = name.lower()

print("\nIs name == 'jim'? I predict True.")
print(l_name == "jim")

print("\nIs name == 'Jim'? I predict False.")
print(l_name == "Jim")
# 3 Numerical Tests
big_num = 100
small_num = 1
max_num = 100

print("\nIs big_num == '100'? I predict True.")
print(big_num == 100)

print("\nIs big_num == '101'? I predict False.")
print(big_num == 101)

print("\nIs big_num < small_num? I predict False.")
print(big_num < small_num)

print("\nIs big_num > small_num? I predict True.")
print(big_num > small_num)

print("\nIs big_num >= max_num? I predict True.")
print(big_num >= max_num)

print("\nIs big_num <= max_num? I predict True.")
print(big_num <= max_num)
# 4 Tests using 'and' and 'or'
print("\nIs (big_num >= max_num) and (big_num >= small_num)? I predict True.")
print((big_num >= max_num) and (big_num >= small_num))

print("\nIs (big_num <= max_num) or (big_num >= small_num)? I predict True.")
print((big_num <= max_num) or (big_num >= small_num))
# 5
brand = ["Gucci", "Lacoste", "LV"]

print("\nBrand list:")
print(brand)
print("\nDoes Gucci exist in list ")
print("Gucci" in brand)

brand = ["Gucci", "Lacoste", "LV"]
print("\nDoes Nike exist in list ")
print("Nike" in brand)
