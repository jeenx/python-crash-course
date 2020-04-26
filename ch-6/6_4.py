# Exercise 6-4. Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your series of
# print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.


programming_words = {
    "Dictionary": "a collection of data values",
    "List": " a mutable, or changeable, ordered sequence of elements",
    "Set": "contains an unordered collection of unique and immutable objects",
    "Max": "Return the largest item in an iterable or the largest of two or more arguments.",
    "Min": "Return the smallest item in an iterable or the smallest of two or more arguments.",
    "Lazy": "I'm too lazy to come up with new words and meanings",
}

for word, definition in programming_words.items():
    print(f"{word}:\n\t{definition}\n")
