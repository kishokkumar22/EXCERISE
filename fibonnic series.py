def fibonacci_series(Str):
    list1 = [0, 1]
    for i in range(2, Str):
        list1.append(list1[-1] + list1[-2])
    return list1


n = int(input("Enter the value : "))
print(fibonacci_series(n))
