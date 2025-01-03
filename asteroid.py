import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2


"""
Extending the project
You've done all the required steps, but if you'd like to make the project your own, here are some ideas:

Add a scoring system
Implement multiple lives and respawning
Add an explosion effect for the asteroids
Add acceleration to the player movement
Make the objects wrap around the screen instead of disappearing
Add a background image
Create different weapon types
Make the asteroids lumpy instead of perfectly round
Make the ship have a triangular hit box instead of a circular one
Add a shield power-up
Add a speed power-up
Add bombs that can be dropped
"""
