def reverse_words(Str1):
    reversed_word = ""
    word = ""
    for char in Str1:
        if char != " ":
            word += char
        else:
            reversed_word = word + " " + reversed_word
            word = ""
    reversed_word = word + " " + reversed_word
    return reversed_word.strip()

Str = "Hello Python Programming World"
print(reverse_words(Str))