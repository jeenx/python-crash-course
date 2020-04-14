# Exercise 3-6. More Guests: You just found a bigger dinner table, so now more
#  space is available. Think of three more guests to invite to dinner.
"""
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() 
call to the end of your program informing people that you found a bigger
 dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list
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
