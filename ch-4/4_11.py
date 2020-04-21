# Exercise 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise
# 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
"""
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas 
are:, and then use a for loop to print the first list. Print the message My 
friend’s favorite pizzas are:, and then use a for loop to print the second 
list. Make sure each new pizza is stored in the appropriate list.
"""
# From Exercise 4-1
favorite_pies = ["pepperoni", "hawaiian", "cheese"]

for pie in favorite_pies:
    print(f"I like {pie} pizza")

print("\nI really love pizza!\n")

# Exercise 4-11
favorite_pies.append("cheese crust")

friend_pizzas = []
friend_pizzas.append("Veggie")

print("My favorite pizzas are:")
for pie in favorite_pies:
    print(pie)

print("\nMy friend's favorite pizzas are:")
for pizzas in friend_pizzas:
    print(pizzas)
