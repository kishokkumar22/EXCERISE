# find the middle element in a list.

def midelement(num1):
    midlist = int(len(num1)//2)
    print(midlist)
    return print("The middle element in a list is : ", num1[midlist])

num = []
a = int(input("Enter the range : "))
for i in range(a):
    b = int(input("Enter the value : "))
    num.append(b)

midelement(num)