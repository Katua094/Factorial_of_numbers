# Recursion with Python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Accept user input for the number
n = int(input("Enter a number: "))

# Calculate and print the factorial
result = factorial(n)
print(f"The factorial of {n} is: {result}")
