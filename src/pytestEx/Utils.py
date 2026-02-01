def root(num):
    return num ** 0.5

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base, exponent):
    return base ** exponent

def modulus(a, b):
    return a % b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0


def dictionary_fixture():
    return {"Name": "Karan", "Age": 30, "City": "New York"}