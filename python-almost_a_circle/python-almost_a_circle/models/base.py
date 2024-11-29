import json

class Base:
    """Base class for all other classes in the project"""
    
    # Private class attribute to track number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class
        
        Args:
            id (int, optional): Identifier for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert list of dictionaries to JSON string
        
        Args:
            list_dictionaries (list): List of dictionaries
        
        Returns:
            str: JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation to a file
        
        Args:
            list_objs (list): List of instances
        """
        filename = cls.__name__ + ".json"
        
        # Convert objects to dictionaries
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        
        # Write JSON string to file
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert JSON string to list of dictionaries
        
        Args:
            json_string (str): JSON string representation
        
        Returns:
            list: List of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set
        
        Args:
            **dictionary: Double pointer to a dictionary
        
        Returns:
            Instance with attributes set
        """
        # Create a "dummy" instance
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        
        # Update with real attributes
        dummy.update(**dictionary)
        return dummy
