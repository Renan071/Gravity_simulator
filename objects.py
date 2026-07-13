import math

class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def multk(self, k):
        return Vec(self.x*k, self.y*k)
    
    def divide(self, k):
        return Vec(self.x/k, self.y/k )
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def normalize(self):
        mag = self.magnitude()
        return Vec(self.x/mag, self.y/mag)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Body:
  
    def __init__(self, position, velocity, mass):
        self.position = position #vector (x, y)
        self.velocity = velocity # vector (x, y)
        self.mass = mass # mass in kilograms
        self.force = Vec(0, 0)



    

