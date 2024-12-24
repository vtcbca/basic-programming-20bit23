import math

def factorial_math_module(n):
    return math.factorial(n)

num = int(input("Enter a number: "))
print(f"Factorial using math module: {factorial_math_module(num)}")
