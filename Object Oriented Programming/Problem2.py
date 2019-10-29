#A PROGRAM THAT CREATES A CYLINDER CLASS WHICH HAS A volume AND surface_area METHODS
import math

class Cylinder:

    def __init__(self,height=1,radius=1):
        #initializes the cylinder class
        self.height = height
        self.radius = radius

    def volume(self):
        #calcualtes and returns volume V = (pi)(r^2)(h)
        return math.pi * (self.radius**2) * self.height
    def surface_area(self):
        #calculates and returns surface area A=2πrh+2πr^2
        return (2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius**2))

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
