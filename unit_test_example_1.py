import inspect
import doctest
import re
import math
import unittest

# Define below the class 'Circle' and it's methods with proper doctests.
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

class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # the value of c1.radius equal to 2.5 or not
        c1 = Circle(2.5)
        self.assertEqual(c1.radius, 2.5)

    def test_creating_circle_with_negative_radius(self):
        # Try Defining a circle 'c' with radius -2.5 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"
        with self.assertRaises(ValueError) as error:
        	c = Circle(-2.5)
        	c.area()
        	self.assertEqual("radius must be between 0 and 1000 inclusive" in error)

    def test_creating_circle_with_greaterthan_radius(self):
        # Try Defining a circle 'c' with radius 1000.1 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"   
        with self.assertRaises(ValueError) as error:
        	c = Circle(1000.1)
        	c.circumference()
        	self.assertEqual("radius must be between 0 and 1000 inclusive" in error)
        

    def test_creating_circle_with_nonnumeric_radius(self):
        # Try Defining a circle 'c' with radius 'hello' and see 
        # if it raises a TypeError with the message
        # "radius must be a number"
        with self.assertRaises(TypeError) as error:
        	c = Circle("Hello")
        	self.assertEqual("radius must be a number" in error)     
