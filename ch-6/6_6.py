# Exercise 6-6. Polling: Use the code in favorite_languages.py (page 97).
"""
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding. If they 
have not yet taken the poll, print a message inviting them to take the poll.
"""
# favorite_languages (page 97)
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

polled_person = ["phil", "obama", "sarah", "mike"]

for person in polled_person:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for your response")
    else:
        print(f"{person.title()}, no response yet. Feel free to take the poll.")
