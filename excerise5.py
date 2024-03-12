# Find the Maximum number in the list.

def maximumNumber(n):
    maxNum = n[0]
    for num in n:
        if maxNum < num:
            maxNum = num
    return maxNum


def maximumNumber2(num2):
    list2 = sorted(num2)
    list3 = list2[-1]
    return list3


num1 = []
a = int(input("Enter the range : "))
for j in range(a):
    b = int(input("Enter the Value : "))
    num1.append(b)
print("The Maximum number using hardcode method : ", maximumNumber(num1))
print("The Maximum number using Function method : ", maximumNumber2(num1))
