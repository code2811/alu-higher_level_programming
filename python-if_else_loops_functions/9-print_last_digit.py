def print_last_digit(number):
    """
    Prints and returns the last digit of a number
    
    Args:
        number: The input number (can be positive or negative)
    
    Returns:
        The value of the last digit
    """
    # Convert number to positive to handle negative numbers
    last_digit = abs(number) % 10
    # Print the last digit without newline
    print(last_digit, end="")
    return last_digit
