#--------bodies--------- 
from vectors import vec
#real moon distance 405507000 in meters
# 5.97219e24 earth mass
# 7.34767e22 moon mass

class body:
    def __init__(self, mass, position, velocity, acceleration):
        self.mass = mass
        self.position = position #vector (x, y)
        self.velocity = velocity #vector (vx, vy)
        self.acceleration = acceleration # calculated dynamically vector (ax, ay)
        
earth = body(
    2e10,
    vec(0, 0),
    vec(0, 0),
    vec(0, 0)
)
moon = body(
    7e8,
    vec(4, 3),
    vec(0, 0),
    vec(0, 0)
)