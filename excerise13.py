def reverse_words(input_str):
    words = input_str.split()  # Split the string into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_str = ' '.join(reversed_words)  # Join the reversed words back together with spaces
    return reversed_str

input_str = input("Enter the string: ")
print(reverse_words(input_str))
