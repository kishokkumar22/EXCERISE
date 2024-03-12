# Counting the number of occurrence a character in the given word.
word = "Programming"
letter = "P"
count = 0
for character in word:
    if letter == character:
        count += 1
print(count)
