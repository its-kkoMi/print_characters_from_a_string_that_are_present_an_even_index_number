# Assignment 5 - Exercise 3
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# Ask user for input

word = str(input("Enter word/s: "))

# Convert string to list
# Use list slicing
# Print even index characters

print("\nEven Index Characters: \n")

index_characters = list(word)
for i in index_characters[0::2]:
    print(i)