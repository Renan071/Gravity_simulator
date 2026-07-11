import math
from vectors import vec
from bodies import earth
from bodies import moon
#-------------------------#

G = 6.67430e-11

def gravitational_force(G, mass1, mass2, distance):
    force = (G*mass1*mass2)/distance**2
    return force

def f_vector(force, unit_direction):
    force_vector = unit_direction * force 
    return force_vector

def acceleration(mass, f_vector ):
    return f_vector/mass

def distance(direction):
    distance = direction.magnitude()
    return distance

mass1 = earth.mass
mass2 = moon.mass

direction = moon.position - earth.position

force = gravitational_force(G, mass1, mass2, distance(direction))

unit_direction = direction/direction.magnitude()

force_on_earth = f_vector(force, unit_direction)
force_on_moon = f_vector(force, unit_direction)*-1

earth_acceleration = acceleration(earth.mass, force_on_earth) 
moon_acceleration = acceleration(moon.mass, force_on_moon)*-1

result = f_vector(gravitational_force(G, mass1, mass2, distance(direction)), unit_direction)

# print(gravitational_force(G, mass1, mass2, distance(vec1, vec2)))
# print(acceleration(mass1, mass2, gravitational_force(G, mass1, mass2, distance(vec1, vec2))))
#print(distance(vec1, vec2))
# print(f_vector(gravitational_force(G, mass1, mass2, distance(direction)), unit_direction))
# print((result.x, result.y))
# print((moon_acceleration.x, moon_acceleration.y))
# print((earth_acceleration.x, earth_acceleration.y))