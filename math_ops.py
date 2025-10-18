def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a / b


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def average(numbers):
    if len(numbers) == 0:
        raise ZeroDivisionError()
    return sum(numbers) / len(numbers)