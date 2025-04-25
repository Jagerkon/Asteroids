import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot



def main():
    pygame.init()
    #initializing game objects

    #creating screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #creating clock
    clock = pygame.time.Clock()

    #creating sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    #creating player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #creating AsteroidField object
    asteroid_field = AsteroidField()

    dt = 0
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update player
        updatable.update(dt)

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # update collision check
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over")
                sys.exit()
            
            # update bullet collision check
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()

        #60 fps
        dt = clock.tick(60) / 1000  # seconds


if __name__ == "__main__":
    main()