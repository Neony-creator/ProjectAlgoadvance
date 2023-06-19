import random

import toolbox


def evaluate(cities, paths):
    scores = []
    coordinates_i = []
    coordinates_j = []

    for index, path in enumerate(paths):
        score = 0
        coords_i = []
        coords_j = []

        for i in range(len(path) - 1):
            coords_i.append(path[i])
            coords_j.append(path[i+1])
            score += toolbox.euclidean_distance(cities[path[i]], cities[path[i+1]])
        scores.append(score)
        coordinates_i.append(coords_i)
        coordinates_j.append(coords_j)

    best = scores.index(min(scores))

    return (coordinates_i[best], coordinates_j[best]), paths[best], scores[best]

def choose_next_city(probability, available, current):
    a = [probability[current][i] for i in available]
    b = sum(a)
    p = [a[i]/b for i in range(len(a))]
    return random.choices(range(len(p)), weights=p, k=1)[0]

def update(pheromone, alpha, villes, beta):
    securite = 1e-6

    return [
        [
            (pheromone[i][j] ** alpha)
            * (1 / ((toolbox.euclidean_distance(villes[i], villes[j]) or securite) ** beta))
            if i != j
            else 0
            for j in range(len(pheromone))
        ]
        for i in range(len(pheromone))
    ]

def aco(cities, iterations, ants, evaporation, alpha, beta, intensification):

    best_path = []
    best_path_coords = []
    best_score = 0

    pheromone = [[1] * len(cities) for _ in range(len(cities))]

    probability = update(pheromone, alpha, cities, beta)
    available_cities = list(range(len(cities)))

    for i in range(iterations):
        paths = []
        path = []
        for ant in range(ants):
            current_city = 0
            path.append(current_city)

            for a in range(len(available_cities), 0, -1):
                available_cities.remove(current_city)
                if len(available_cities) > 0:
                    current_city = available_cities[choose_next_city(probability, available_cities, current_city)]
                    path.append(current_city)

            path.append(0)
            available_cities = list(range(len(cities)))
            paths.append(path)
            path = []

        best_path_coords, best_path, best_score = evaluate(cities, paths)

        for c in range(len(pheromone)):
            for c2 in range(len(pheromone)):
                pheromone[c][c2] *= evaporation

        for z in range(len(best_path_coords[0])):
            pheromone[best_path_coords[0][z]][best_path_coords[1][z]] += intensification

        probability = update(pheromone, alpha, cities, beta)

    return best_path_coords, best_path, best_score

def kcamions(cluster, cities, iterations, ants, evaporation, alpha, beta, intensification):

    vmeans = toolbox.kmeans(cluster, cities)
    # cities[0] = [50, 50]
    # vmeans = toolbox.pie(cluster, cities)
    vmeans_sub = toolbox.get_sublists(vmeans)

    best_paths = []
    best_paths_coords = []
    best_scores = []
    clusters = []

    for v in range(len(vmeans_sub)):

        current_cluster = [cities[i] for i in vmeans_sub[v]]
        current_cluster.insert(0, cities[0])

        clusters.append(current_cluster)

        pheromone = [[1] * len(current_cluster) for _ in range(len(current_cluster))]

        probability = update(pheromone, alpha, current_cluster, beta)
        available_cities = list(range(len(current_cluster)))

        for i in range(iterations):
            paths = []
            path = []
            for ant in range(ants):
                current_city = 0
                path.append(current_city)

                for a in range(len(available_cities), 0, -1):
                    available_cities.remove(current_city)
                    if len(available_cities) > 0:
                        current_city = available_cities[choose_next_city(probability, available_cities, current_city)]
                        path.append(current_city)

                path.append(0)
                available_cities = list(range(len(current_cluster)))
                paths.append(path)
                path = []

            best_path_coords, best_path, best_score = evaluate(current_cluster, paths)

            for c in range(len(pheromone)):
                for c2 in range(len(pheromone)):
                    pheromone[c][c2] *= evaporation

            for z in range(len(best_path_coords[0])):
                pheromone[best_path_coords[0][z]][best_path_coords[1][z]] += intensification

            probability = update(pheromone, alpha, current_cluster, beta)

        best_paths.append(best_path)
        best_scores.append(best_score)

    return best_paths, best_scores, clusters