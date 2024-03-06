import numpy as np
import random

def calculate_distance(locations,food_location):

    coefficients = np.array([1,1,-2*food_location[0],-2*food_location[1],food_location[0]**2,food_location[1]**2])

    arguments = np.vstack((locations**2, locations,np.ones((locations.shape[0],locations.shape[1]))))

    distances = coefficients@arguments
    return distances

def update_locations(locations,velocilies,c1,c2,Group_best,Personal_best,food_location,old_distances,itterration,max_itter,max_theta,min_theta):

    r1 = random.uniform(0,1)
    r2 = random.uniform(0,1)
    Group_best = Group_best.reshape((2,1))
    theta = max_theta - ((max_theta-min_theta)/max_itter)*itterration

    new_velocity = theta*velocilies + c1*r1*(Personal_best-locations) + c2*r2*(Group_best-locations)
    ## keep inside the region
    new_locations = locations + new_velocity

    new_distances = calculate_distance(new_locations,food_location)
    new_group_best_index = np.argmin(new_distances)
    New_Group_best = new_locations[:,new_group_best_index]

    condition = new_distances < old_distances
    Personal_best[:, condition] = new_locations[:, condition]

    return new_velocity,new_locations,New_Group_best,Personal_best