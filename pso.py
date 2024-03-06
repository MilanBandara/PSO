import pygame
import sys
import random
import math
import numpy as np
from helper import calculate_distance,update_locations
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 5
PARTICLE_RADIUS = 5
PARTICLE_COLOR = (255, 0, 0)
FOOD_COLOR = (0,255,0)
BG_COLOR = (255, 255, 255)


# Create particles
num_particles = 1000
food_location = (100,100)
max_itter = 1000
max_theta = 1
min_theta = 0
dimension = 2

#initializa the initial velocities as zero
velocilies = np.zeros((dimension,num_particles))
#initialize random locations
locations = np.random.uniform(0,1, (dimension,num_particles))
locations[0,:] = locations[0,:]*WIDTH
locations[1,:] = locations[1,:]*HEIGHT

#evaluate initial function values of all particles
distances = calculate_distance(locations,food_location)

#find the initial best personal positions and droup positions
group_best_index = np.argmin(distances)
Group_best = locations[:,group_best_index]
Personal_best = locations ## take the initial positions as the initial personal best positions

c1 = 0.5
c2 = 0.5


# Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Particle Swarm Optimization')

# Main loop
clock = pygame.time.Clock()
running = True
itterration = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(BG_COLOR)
    print(itterration)
    pygame.draw.circle(screen, FOOD_COLOR, (int(food_location[0]), int(food_location[1])), PARTICLE_RADIUS)
    # Draw particles >> ittterate the
    for index,location in enumerate(locations.T):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(location[0]), int(location[1])), PARTICLE_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    #update the locations
    velocilies,locations,Group_best,Personal_best = update_locations(locations,velocilies,c1,c2,Group_best,Personal_best,food_location,distances,itterration,max_itter,max_theta,min_theta)
    itterration = itterration + 1
# Quit Pygame
pygame.quit()
sys.exit()
