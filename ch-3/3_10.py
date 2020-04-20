# 3-10. Every Function: Think of something you could store in a list. For
# example, you could make a list of mountains, rivers, countries, cities,
# languages, or any- thing else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this chapter
# at least once.

cities = ["Irvine", "Santa Ana", "Mission Viejo", "Laguna Beach", "Santa Monica"]

print(cities)

print(f"Name of cities in Orange County: {cities}\n")

print(f"Uh Oh - Santa Monica is in LA")

del cities[4]
cities.insert(4, "Tustin")
print(f"List has been corrected: {cities}")

print(f"Temporarily sorting list alphabetically: {sorted(cities)}")

print(f"Temporarily reversing sorted list: {sorted(cities, reverse=True)}")

print(f"Removing {cities.pop()} from the list")

cities.reverse()
print(f"Reversing list: {cities}")

cities.sort()
print(f"Sorting list: {cities}")
