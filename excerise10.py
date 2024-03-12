def anagram(num1, num2):

    num1 = sorted(list(num1.lower()))
    num2 = sorted(list(num2.lower()))
    if num1 == num2:
        return print(f"The given word is an anagram")
    else:
        return print(f"The given word is not an anagram")


str0 = input("Enter the String : ")
str1 = input("Enter the String : ")
anagram(str0, str1)
