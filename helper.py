import numpy as np
import random

def calculate_distance(locations,food_location):

    coefficients = np.array([1,1,-2*food_location[0],-2*food_location[1],food_location[0]**2,food_location[1]**2])

    arguments = np.vstack((locations**2, locations,np.ones((locations.shape[0],locations.shape[1]))))

    distances = coefficients@arguments
    return distances

def update_locations(locations,velocilies,c1,c2,Group_best,Personal_best):

    r1 = random.uniform(0,1)
    r2 = random.uniform(0,1)
    test1 = Personal_best-locations
    
    test2 = Group_best-locations
    # new_velocity = velocilies + c1*r1*(Personal_best-locations) + c2*r2*(Group_best-locations)
    # new_locations = locations + new_velocity