# Exercise  3-7. Shrinking Guest List: You just found out that your new dinner
#  table won’t arrive in time for the dinner, and you have space for only two
# guests.
"""
• Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names 
remain in your list. Each time you pop a name from your list, print a message 
to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them 
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program.
"""


guest_list = ["Chester Bennington", "Napolean Bonaparte", "Kurt Cobain"]

print(f"{guest_list[0]}, would you like to come over for dinner?")
print(f"{guest_list[1]}, would you like to come over for dinner?")
print(f"{guest_list[2]}, would you like to come over for dinner?")

print(f"\n{guest_list[1]} will not be able to make it\n")
del guest_list[1]
guest_list.insert(1, "Steve Carell")

print(f"{guest_list[0]}, would you like to come over for dinner?")
print(f"{guest_list[1]}, would you like to come over for dinner?")
print(f"{guest_list[2]}, would you like to come over for dinner?")

print(f"\nHey everybody I found a bigger dinner table!\n")

guest_list.insert(0, "Mike Shinoda")
guest_list.insert(2, "Eiichiro Oda")
guest_list.append("Akira Toriyama")

print(f"{guest_list[0]}, would you like to come over for dinner?")
print(f"{guest_list[1]}, would you like to come over for dinner?")
print(f"{guest_list[2]}, would you like to come over for dinner?")
print(f"{guest_list[3]}, would you like to come over for dinner?")
print(f"{guest_list[4]}, would you like to come over for dinner?")
print(f"{guest_list[5]}, would you like to come over for dinner?")

print(
    f"\nHey everybody, bad news! The dinner table won't be here on time. I "
    "can only invite two guests"
)

print(f"My apologies, {guest_list.pop()}, you are removed from the list")
print(f"My apologies, {guest_list.pop()}, you are removed from the list")
print(f"My apologies, {guest_list.pop()}, you are removed from the list")
print(f"My apologies, {guest_list.pop()}, you are removed from the list")

print(f"{guest_list[0]}, you are still in the guest list")
print(f"{guest_list[1]}, you are still in the guest list")

del guest_list[0]
del guest_list[0]

print(f"\nDisplaying current list values: ")
print(guest_list)
