my_rectangle1 = Rectangle(8, 4)
print(my_rectangle1)

Rectangle.print_symbol = "C"
print(my_rectangle1)

my_rectangle2 = Rectangle(2, 1)
print(my_rectangle2)

my_rectangle1.print_symbol = "H"
print(my_rectangle1)
print(my_rectangle2)

Rectangle.print_symbol = "K"
print(my_rectangle2)

my_rectangle1.print_symbol = 89
print(my_rectangle1)

my_rectangle1.print_symbol = ["Holberton", "School"]
print(my_rectangle1)

