from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle
        
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): Identifier. Defaults to None.
        """
        # Call parent constructor
        super().__init__(id)
        
        # Validate and set attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle using '#' character"""
        # Print vertical offset
        for _ in range(self.__y):
            print()
        
        # Print rectangle
        for _ in range(self.__height):
            # Print horizontal offset
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """String representation of Rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update rectangle attributes
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        
        # Update using positional arguments
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        
        # Update using keyword arguments
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
            'x': self.x,
            'y': self.y, 
            'id': self.id, 
            'height': self.height, 
            'width': self.width
        }
