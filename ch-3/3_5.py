# Exercise 3-5. Changing Guest List: You just heard that one of your guests
# can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
"""
• Start with your program from Exercise 3-4. Add a print() call at the end of 
your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
 name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still 
in your list.
"""

guest_list = ["Chester", "Napolean", "Kurt"]

print(f"{guest_list[0]}, would you like to come over for dinner?")
print(f"{guest_list[1]}, would you like to come over for dinner?")
print(f"{guest_list[2]}, would you like to come over for dinner?")

print(f"\n{guest_list[1]} will not be able to make it\n")
del guest_list[1]
guest_list.insert(1, "Carell")

print(f"{guest_list[0]}, would you like to come over for dinner?")
print(f"{guest_list[1]}, would you like to come over for dinner?")
print(f"{guest_list[2]}, would you like to come over for dinner?")
