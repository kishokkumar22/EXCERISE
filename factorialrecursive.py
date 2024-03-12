import math as mt
def factorial(fact):
    if fact <= 1:
        return 1
    return fact*factorial(fact-1)

fact1 = int(input("Enter the number : "))
print(factorial(fact1))

print(f"Factorial of {fact1} is : ", mt.factorial(fact1))
