import pygame
import random
from circleshape import CircleShape
from constants import *

# Base Class for player object
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt
        
    def split(self):
        # Split the asteroid into two smaller asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_clockwise = self.velocity.rotate(angle)
        vector_counterclockwise = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_clockwise = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_counterclockwise = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_clockwise.velocity = vector_clockwise * 1.2
        new_asteroid_counterclockwise.velocity = vector_counterclockwise * 1.2