try:
    my_rectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.width = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.width = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.height = -4
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, 3)
    my_rectangle.height = "4"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(2, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle("2", 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Other expected output cases
my_rectangle = Rectangle(2, 4)
print(sorted(my_rectangle.__dict__))

my_rectangle = Rectangle(2, 4)
print(my_rectangle.width)

my_rectangle = Rectangle(2, 4)
print(my_rectangle.height)

my_rectangle = Rectangle(4)
print("{} - {}".format(my_rectangle.width, my_rectangle.height))

my_rectangle = Rectangle()
print("{} - {}".format(my_rectangle.width, my_rectangle.height))

my_rectangle = Rectangle(2, 4)
print("{} - {}".format(my_rectangle.width, my_rectangle.height))
my_rectangle.width = 10
print("{} - {}".format(my_rectangle.width, my_rectangle.height))

my_rectangle = Rectangle(2, 4)
print("{} - {}".format(my_rectangle.width, my_rectangle.height))
my_rectangle.height = 10
print("{} - {}".format(my_rectangle.width, my_rectangle.height))

