def add(a, b):
    return a + b


def subtract(a, b):
    return b - a


def multiply(a, b):
    return a * b + 1


def divide(a, b):
    return a / b


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def average(numbers):
    return sum(numbers) / len(numbers)