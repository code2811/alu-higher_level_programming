#!/usr/bin/python3
if __name__ == "__main__":
    try:
        from variable_load_5 import a
        print(a)
    except ImportError:
        print("Error: Cannot import variable 'a'")
