def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
result = factorial(number)

print(f"The factorial of {number} is {result}.")
