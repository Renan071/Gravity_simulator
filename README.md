# Gravity Simulator

A personal project developed in Python to study gravitational physics, vector mathematics, and numerical simulation.

The goal of this project is to build a gravitational simulator from scratch, implementing the mathematics behind the interaction between bodies and orbital mechanics.

## Current Features

- Vector class implementation  
- Vector addition, subtraction and scalar multiplication  
- Vector magnitude calculation  
- Distance calculation between bodies  
- Newtonian gravitational force calculation  
- Force represented as a vector  
- Acceleration calculation from force and mass  
- Velocity updates using half-kick integration method  
- Position updates with numerical integration  
- Complete simulation loop with time warping  
- Graphical interface with matplotlib visualization  
- Multi-body orbital simulation (Sun, Mercury, Venus, Earth, Moon, Mars, Asteroid)  

## Project Structure

- `gravity_sim.py` - Main simulation script with visualization
- `objects.py` - Vector and Body class implementations

## Physics Implemented

The gravitational force between two bodies is calculated using Newton's law of universal gravitation:

$$
F = G \frac{m_1 m_2}{r^2}
$$

where:

- $F$ is the gravitational force
- $G$ is the gravitational constant
- $m_1$ and $m_2$ are the masses of the bodies
- $r$ is the distance between them

The force direction is represented using vectors. The acceleration of a body is calculated using:

$$
a = \frac{F}{m}
$$

### Numerical Integration

The simulation uses a **half-kick integration method** to update velocities and positions:

1. Calculate forces on all bodies
2. Update velocities with half timestep acceleration
3. Update positions using full timestep with updated velocities
4. Recalculate forces at new positions
5. Update velocities with another half timestep acceleration

## Future Goals

- Improve accuracy with higher-order integration methods
- Add collision detection and merging
- Optimize performance for larger n-body systems
- Add user controls for real-time parameter adjustment
- Export trajectories for analysis
- Add trails to visualize orbital paths
- Enhance graphical interface with zoom and pan controls

## Purpose

This project is mainly focused on learning and experimenting with:

- Python
- Object-oriented programming
- Vector mathematics
- Classical mechanics
- Numerical simulation
- Software development practices

## Status

Active development (v1 nearly finished)
