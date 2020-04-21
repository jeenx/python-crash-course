# Exercise 4-5. Summing a Million: Make a list of the numbers from one to one
# million, and then use min() and max() to make sure your list actually starts
# at one and ends at one million. Also, use the sum() function to see how
# quickly Python can add a million numbers.

num_list = list(range(1, 1_000_001))

print(min(num_list))
print(max(num_list))
print(sum(num_list))
