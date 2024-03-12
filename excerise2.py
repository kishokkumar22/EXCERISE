# Count consonants in the word
vowel = ['a', 'e', 'i', 'o', 'u']
word = "Programming"
consonant = []
for character in word:
    if character not in vowel:
        consonant.append(character)
print(consonant)
