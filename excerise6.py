# Find the minimum number in the list.
def minNumber1(num):
    minNum = num[0]
    for n in num:
        if minNum > n:
            minNum = n
    return minNum


def minNumber2(num1):
    list1 = sorted(num1)
    list2 = list1[0]
    return list2


empty1 = []
range1 = int(input("Enter the range : "))
for i in range(range1):
    a = int(input("Enter the value : "))
    empty1.append(a)
print("The minimum number was fetch by using Inbuilt function method : ", minNumber2(empty1))
print("The minimum number was fetch by using hardcode method         : ", minNumber1(empty1))
