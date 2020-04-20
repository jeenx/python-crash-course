# Exercise 3-8. Seeing the World: Think of at least five places in the world
# you’d like to visit.
"""
• Store the locations in a list. Make sure the list is not in alphabetical 
order.
• Print your list in its original order. Don’t worry about printing the list 
neatly, just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the 
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without 
changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that
its order has changed.
• Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print 
the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order. 
Print the list to show that its order has changed.
"""

locations = ["Orlando", "Tokyo", "South Korea", "Boston", "London"]

print(f"Original list: {locations}")

print(f"Temp sorted list: {sorted(locations)}")

print(f"Verifying original list: {locations}")

print(f"Temp reverse sorted list: {sorted(locations, reverse=True)}")

print(f"Verifying original list: {locations}")

locations.reverse()
print(f"Reversing original list permanently: {locations}")

locations.reverse()
print(f"Reversing modified list back to original: {locations}")

locations.sort()
print(f"Permanently sorting list alphabetically: {locations}")

locations.sort(reverse=True)
print(f"Permanently sorting list alphabetically: {locations}")
