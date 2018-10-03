import inspect
import re
import unittest
import math


# Define below the class 'Circle' and it's methods.
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
        
class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # it's circumference is 15.71
        c1= Circle(2.5)
        self.assertEqual(c1.circumference(), 15.71)
        
    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0 and check if 
        # it's circumference is 0.
        c2= Circle(0)
        self.assertEqual(c2.circumference(), 0)
        
    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000 and check if 
        # it's circumference is 6283.19.
        c3= Circle(1000)
        self.assertEqual(c3.circumference(), 6283.19)
        
