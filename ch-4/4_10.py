# Exercise 4-10. Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:
"""
• Print the message The first three items in the list are:. Then use a slice to
 print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print
 the last three items in the list.
"""

animals = ["cat", "dog", "horse"]

for animal in animals:
    print(f"A {animal} can run very fast")

print("All these animlas have four legs!")
# Exercise 4-10:
print(f"The first three items in the list are: {animals[0:3]}")
# confused on this question since list has a total of 3 items
print(f"Three items from the middle of the list are: {animals[1:2]}")
print(f"The last three items in the list are {animals[-3:]}")
