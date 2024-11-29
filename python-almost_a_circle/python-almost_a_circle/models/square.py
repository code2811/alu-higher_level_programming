from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square
        
        Args:
            size (int): Size of square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): Identifier. Defaults to None.
        """
        # Call parent constructor with size for width and height
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square attributes
        
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        attrs = ['id', 'size', 'x', 'y']
        
        # Update using positional arguments
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    if i == 1:  # size corresponds to width/height
                        setattr(self, 'width', value)
                        setattr(self, 'height', value)
                    else:
                        setattr(self, attrs[i], value)
        
        # Update using keyword arguments
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                elif key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.size
        }
