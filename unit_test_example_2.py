import inspect
import re
import unittest
import math

class Circle:
    
    def __init__(self, radius):
        # Define the initialization method below
        pattern = re.compile("^\\-?[0-9]")
        if(pattern.match(str(radius))):
            if(radius >= 0 and radius <= 1000):
                self.radius = radius
            else:
                raise ValueError("radius must be between 0 and 1000 inclusive")
        else:
            raise TypeError("radius must be a number")
        
        
    def area(self):
        # Define the area functionality below
        return round(((self.radius ** 2) * math.pi),2)

    def circumference(self):
        # Define the circumference functionality below
        return round((self.radius * 2 * math.pi),2)
        
class TestCircleArea(unittest.TestCase):
    
    def test_circlearea_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # it's area is 19.63
        c1 = Circle(2.5)
        self.assertEqual(c1.area(), 19.63)
        
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0 and check if 
        # it's area is 0
        c2 = Circle(0)
        self.assertEqual(c2.area(), 0)
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1 and check if 
        # it's area is 3141592.65
        c3 = Circle(1000)
        self.assertEqual(c3.area(), 3141592.65)
