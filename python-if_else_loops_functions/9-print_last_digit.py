def print_last_digit(number):
    """
    Prints and returns the last digit of a number
    Args:
        number: The input number (can be positive or negative)
    Returns:
        The last digit of the number
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
