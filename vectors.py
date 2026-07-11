import math
#----------------------------
class vec:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return vec(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return vec(k*self.x, k*self.y)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __truediv__(self, k):
        return vec(self.x/k, self.y/k)