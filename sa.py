import random
import  time


import numpy

import toolbox

def distance_total(path):
    dist=0
    for i in range(len(path) - 1):
        dist += toolbox.euclidean_distance(path[i], path[i + 1])
    return dist


def sa(temperature, cx_regretion, iterations, cities_coords):
    start_timer=time.time()

    best_val = distance_total(cities_coords)

    for i in range(iterations):
        start_iter = time.time()
        start_process_time = time.process_time()
        # Exchange two coordinates and get a new neighbour solution
        c1, c2 = numpy.random.randint(0, len(cities_coords), size=2)
        temp = cities_coords[c1]
        cities_coords[c1] = cities_coords[c2]
        cities_coords[c2] = temp

        # Get the new cost
        evaluate_val = distance_total(cities_coords)
        diff = best_val - evaluate_val
        # calculate metropolis acceptance criterion
        metropolis = numpy.exp((diff) / temperature)
        xrand = numpy.random.uniform()

        if evaluate_val < best_val:
            best_val = evaluate_val
        else:
            rand = numpy.random.uniform()
            if rand < metropolis:
                best_val = evaluate_val
            else:
                temp = cities_coords[c1]
                cities_coords[c1] = cities_coords[c2]
                cities_coords[c2] = temp

        if temperature>0.001:
            temperature = temperature*cx_regretion


    return best_val, cities_coords