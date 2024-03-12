# palindrome
def palindrome1(str1):
    if str1.lower() == str1[::-1].lower():
        return print(f"The given string {str1} is a Palindrome")
    else:
        return print(f"The given string {str1} is not a Palindrome")


def palindrome2(str2):
    reverse_string = ""
    for i in range(len(str2) - 1, -1, -1):
        reverse_string += str2[i]
    if str2.lower() == reverse_string.lower():
        return print(f"The given string {str2} is a Palindrome")
    else:
        return print(f"The given string {str2} is not a Palindrome")


def palindrome3(str3):
    new1 = list(str3)
    new1.reverse()
    string3 = ''.join(new1)
    return string3


string1 = input("Enter the string : ")
# palindrome1(string1)
palindrome2(string1)
print(palindrome3(string1))
