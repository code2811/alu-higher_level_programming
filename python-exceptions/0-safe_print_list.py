#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list and returns number of elements printed
    Args:
        my_list: list of elements
        x: number of elements to print
    Returns:
        The real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print("")
    return coun



