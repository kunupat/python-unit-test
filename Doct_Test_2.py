import inspect
import doctest
import re
import math
# Define below the class 'Circle' and it's methods with proper doctests.
class Circle:
    
    def __init__(self, radius):
        # Define the doctests for __init__ method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius
        
    def area(self):
        # Define the doctests for area method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.area() 
        19.63
        """
        # Define the area functionality below
        return round(((self.radius ** 2) * math.pi),2)
        
        
    def circumference(self):
        # Define the doctests for circumference method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define the circumference functionality below
        return round((self.radius * 2 * math.pi),2)
