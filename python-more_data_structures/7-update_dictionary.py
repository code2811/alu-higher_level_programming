#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Update or add key/value pairs in a dictionary."""
    a_dictionary[key] = value

if __name__ == "__main__":
    # Case 1
    a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
    update_dictionary(a_dictionary, "a", "A")
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'a' / value = 'A'")

    # Case 2
    a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
    update_dictionary(a_dictionary, "e", "E")
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'e' / value = 'E'")

    # Case 3
    a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
    update_dictionary(a_dictionary, "a", 89)
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'a' / value = 89")

    # Case 4
    a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
    update_dictionary(a_dictionary, "e", [1, 2, 3])
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'e' / value = [1, 2, 3]")

    # Case 5
    a_dictionary = {'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}
    update_dictionary(a_dictionary, "f", "A")
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'f' / value = 'A'")

    # Case 6
    a_dictionary = {}
    update_dictionary(a_dictionary, "a", "a")
    print(f"Correct output - case: a_dictionary = {a_dictionary} / key = 'a' / value = 'a'")

