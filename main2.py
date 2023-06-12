import time
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def adjacency_matrix(matrix):
    adj = np.zeros(matrix.shape)


def update(pheromone, alpha, visibility, beta):
    return (pheromone ** alpha) * (visibility ** beta)


def choose_next_city(prob, available, city):
    a = prob[city, available]
    b = np.sum(a)
    p = a/b
    return np.random.choice(range(len(p)), p=p)


def evaluate(matrix, paths):
    scores = np.zeros(len(paths))
    coordinates_i = []
    coordinates_j = []

    for index, path in enumerate(paths):
        score = 0
        coords_i = []
        coords_j = []

        for i in range(len(path) - 1):
            coords_i.append(path[i])
            coords_j.append(path[i + 1])
            score += matrix[path[i], path[i + 1]]
        scores[index] = score
        coordinates_i.append(coords_i)
        coordinates_j.append(coords_j)

    best = np.argmin(scores)

    return (coordinates_i[best], coordinates_j[best]), paths[best], scores[best]


def aoc(matrix, iterations, ants, cities, evaporation, intensification, ):
    start_timer = time.time()
    alpha = 1.0
    beta = 1.0
    # beta_evaporation_rate = 0
    # choose_best = 0.1
    early_stopping_count = 10
    best_score_so_far = 0
    num_equal = 0
    best_series = []
    best_path = 0

    available_cities = list(range(cities))

    # num_equal = 0

    pheromone = np.ones((cities, cities))
    np.fill_diagonal(pheromone, 0)

    visibility = 1/matrix

    probability = update(pheromone, alpha, visibility, beta)

    for i in range(iterations):
        start_iter = time.time()
        paths = []
        path = []

        for ant in range(ants):
            current_city = 0 #available_cities[0] / set_of_available_nodes[np.random.randint(0, len(self.set_of_available_nodes))] #à surveiller / faut penser qu'il faut revenir au point de départ hein
            path.append(current_city)

            for a in range(len(available_cities), 0, -1):
                available_cities.remove(current_city)
                if len(available_cities) > 0:
                    current_city = available_cities[choose_next_city(probability, available_cities, current_city)]
                    path.append(current_city)

            path.append(0)
            available_cities = list(range(cities))
            paths.append(path)
            path = []

        best_path_coords, best_path, best_score = evaluate(matrix, paths)

        if i == 0:
            best_score_so_far = best_score
        else:
            if best_score < best_score_so_far:
                best_score_so_far = best_score

        if best_score == best_score_so_far:
            num_equal += 1
        else:
            num_equal = 0

# self.best_series.append(best_score)
        best_series.append(best_score)
        pheromone *= (1 - evaporation)
        # beta *= (1 - beta_evaporation_rate)
        # pheromone[best_path_coords[0], best_path_coords[1]] += intensification
        probability = update(pheromone, alpha, visibility, beta)

        print("Best score at iteration {}: {}; overall: {} ({}s)"
              "".format(i, round(best_score, 2), round(best_score_so_far, 2),
                        round(time.time() - start_iter)))

        if best_score == best_score_so_far and num_equal == early_stopping_count:
            print("Stopping early due to {} iterations of the same score.".format(early_stopping_count))
            break

    print("End of iterations in : ", time.time() - start_timer)
    best = best_series[np.argmin(best_series)]
    print("ACO finished. Best score: {}".format(best))
    return best_path


if __name__ == '__main__':
    size = 2000
    m = np.random.uniform(1, 10, size=(size, size))



    np.fill_diagonal(m, 0)

    # m *= m

    print("Premier matrice : ", m)
    best = aoc(m, iterations=10, ants=3, cities=size, evaporation=0.1, intensification=2)

    print("Best : ", best)

