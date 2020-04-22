# Exercise 6-3. Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
"""
• Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print 
the word followed by a colon and then its meaning, or print the word on one 
line and then print its meaning indented on a second line. Use the newline 
character (\n) to insert a blank line between each word-meaning pair in your 
output.
"""

programming_words = {
    "Dictionary": "a collection of data values",
    "List": " a mutable, or changeable, ordered sequence of elements",
    "Set": "contains an unordered collection of unique and immutable objects",
    "Max": "Return the largest item in an iterable or the largest of two or more arguments.",
    "Min": "Return the smallest item in an iterable or the smallest of two or more arguments.",
}

print("Dictionary:\n")
print(f"\t{programming_words['Dictionary']}")

print("List:\n")
print(f"\t{programming_words['List']}")

print("Set:\n")
print(f"\t{programming_words['Set']}")

print("Max:\n")
print(f"\t{programming_words['Max']}")

print("Min:\n")
print(f"\t{programming_words['Min']}")
