from objects import Vec
from objects import Body
from itertools import combinations
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.tight_layout
fig.patch.set_facecolor('#10324a')
ax.set_facecolor('black')

ax.grid(True, color = 'navy')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title('n-body simulation', color = 'white')

earth_point, = ax.plot([], [], "bo")
moon_point, = ax.plot([], [], color = "gray", marker = "o")
sun_point, = ax.plot([], [], color = "yellow", marker = "o")
mercury_point, = ax.plot([], [], color = "darkgray", marker = "o")
venus_point, = ax.plot([], [], color = "khaki", marker = "o")
mars_point, = ax.plot([], [], color = "red", marker = "o")
asteroid_point, = ax.plot([], [], color = "white", marker = "o")

plt.ion()
plt.show()

AU = 149597870700
G = 6.6743e-11
dt = 600
time = 0
steps = 0
timewarp = 100

Sun = Body(
    Vec(0, 0),
    Vec(0, 0),
    1.9885e30,
)

Mercury = Body(
    Vec(69816900000, 0),
    Vec(0, 38860),
    3.3011e23,
)

Venus = Body(
    Vec(-108939000000, 0),
    Vec(0, -35260),
    4.8675e24,
)

Earth = Body(
    Vec(152100000000, 0),
    Vec(0, 29290),
    5.9722e24,
)

Moon = Body(
    Vec(-69816900000, 0),
    Vec(0, -55300),
    1e10,
) #Moon used for test instead of the asteroid

Asteroid = Body(
    Vec(500000, 0),
    Vec(0, 61000),
    1e10,
)

Mars = Body(
    Vec(-249261000000, 0),
    Vec(0, -21970),
    6.4171e23,
)

bodies = [Sun, Mercury, Venus, Earth, Moon, Mars, Asteroid]

#===============calculations==================

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

def half_kick(body, dt):
    a = acceleration(body)
    instantaneous_velocity = body.velocity + a.multk(dt/2)
    return instantaneous_velocity

def calculate_forces():
    for body in bodies:
        body.force = Vec(0, 0)

    for body1, body2 in combinations(bodies, 2):
        force_vec = gravitational_force(body1, body2)
        body1.force = body1.force + force_vec
        body2.force = body2.force - force_vec

def physics_step():

    calculate_forces()
    
    for body in bodies:
        body.velocity = half_kick(body, dt)
        
    for body in bodies:
        body.position = body.position + body.velocity.multk(dt)

    calculate_forces()

    for body in bodies:
        body.velocity = half_kick(body, dt)


while time<315360000:
    for _ in range(timewarp):
        physics_step()   
        time += dt
    
    sun_point.set_data([Sun.position.x/AU], [Sun.position.y/AU])
    mercury_point.set_data([Mercury.position.x/AU], [Mercury.position.y/AU])
    venus_point.set_data([Venus.position.x/AU], [Venus.position.y/AU])
    earth_point.set_data([Earth.position.x/AU], [Earth.position.y/AU])
    moon_point.set_data([Moon.position.x/AU], [Moon.position.y/AU])
    mars_point.set_data([Mars.position.x/AU], [Mars.position.y/AU])
    plt.pause(0.001)
    steps += 1


print(f"Tempo simulado: {time}")
print(f"Passos decorridos: {steps}")

#v1 almost finished