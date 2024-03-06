# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:54:26 2024

@author: wooihaw
"""

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def circumference(self):
        return 2 * pi * self.radius
    
c1 = Circle(4)
print(f"Area = {c1.area()}, circumference = {c1.circumference()}")