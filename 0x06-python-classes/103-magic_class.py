import math

class MagicClass:
    """
    A magic class that performs calculations based on radius.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the circle.
        
        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 2 * math.pi * self.__radius

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
