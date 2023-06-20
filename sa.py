import numpy
import toolbox

def distance_total(path):
    return sum(
        toolbox.euclidean_distance(path[i], path[i + 1])
        for i in range(len(path) - 1)
    )


def sa(temperature, cx_regretion, iterations, cities_coords):

    best_val = distance_total(cities_coords)

    for _ in range(iterations):
        # Exchange two coordinates and get a new neighbour solution
        c1, c2 = numpy.random.randint(1, len(cities_coords), size=2)
        temp = cities_coords[c1]
        cities_coords[c1] = cities_coords[c2]
        cities_coords[c2] = temp


        # Get the new cost
        evaluate_val = distance_total(cities_coords)
        diff = best_val - evaluate_val
        # calculate metropolis acceptance criterion

        metropolis = numpy.exp(diff/ temperature)


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

        if temperature>100:
            temperature = temperature*cx_regretion


    return best_val, cities_coords