import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PARTICLE_RADIUS = 5
PARTICLE_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y,WIDTH,HEIGHT,food_location):
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.food_location = food_location
        self.current_distance = None
        self.best_position = float('inf')
        

    # def in_search_space()
    def update(self):

        range_ = 1
        new_x = self.x + random.uniform(-range_, range_)
        new_y = self.y + random.uniform(-range_, range_)

        if (new_x < self.WIDTH or new_x > 0) and (new_y < self.HEIGHT or new_y > 0):
            self.x = new_x
            self.y = new_y
        else:
            self.x = self.x

    def calculate_distance(self,food_location):

        distance = math.sqrt((food_location[0]-self.x)**2 + (food_location[0]-self.y)**2)
        retu
    

# Create particles
num_particles = 30
food_location = (200,200)
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT),WIDTH,HEIGHT,food_location) for _ in range(num_particles)]

#evaluate initial function values of all particles

# Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Particle Swarm Optimization')

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        particle.update()

    # Draw background
    screen.fill(BG_COLOR)

    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(particle.x), int(particle.y)), PARTICLE_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
