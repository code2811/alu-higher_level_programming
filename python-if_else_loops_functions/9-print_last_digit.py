#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the last digit of a number"""
    try:
        last_digit = abs(number) % 10
        print(last_digit, end="")
        return last_digit
    except (TypeError, ValueError):
        raise TypeError("argument must be an integer")
