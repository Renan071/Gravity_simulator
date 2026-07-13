from objects import Vec
from objects import Body
from itertools import combinations
import matplotlib.pyplot as plt

G = 6.6743e-11
dt = 10
time = 0
steps = 0

Earth = Body(
    Vec(2.5, 0),
    Vec(0, -0.001825),
    1e6,
)

Moon = Body(
    Vec(-2.5, 0),
    Vec(0, 0.001825),
    1e6,
)

bodies = [Earth, Moon]

#===============calculatons==================

while time<30000:

    for body in bodies:
        body.force = Vec(0, 0)

    def gravitational_force(body1, body2):
        r_vec = body2.position - body1.position
        distance = r_vec.magnitude()
        direction = r_vec.normalize()
        force_vec = G*body1.mass*body2.mass/distance**2
        force_vector = direction.multk(force_vec)
        return force_vector

    def acceleration(body):
        force = body.force
        mass = body.mass
        accel = force.divide(mass)
        return accel

    def velocity(body, dt):
        a = acceleration(body)
        instantaneous_velocity = body.velocity + a.multk(dt)
        return instantaneous_velocity


    for body1, body2 in combinations(bodies, 2):
        force_vec = gravitational_force(body1, body2)
        body1.force = body1.force + force_vec
        body2.force = body2.force - force_vec
        

    for body in bodies:
        body.velocity = velocity(body, dt)
        body.position = body.position + velocity(body, dt).multk(dt)
        print(body.position)

    time += dt
    steps += 1


print(f"Tempo simulado: {time}")
print(f"Passos decorridos: {steps}")