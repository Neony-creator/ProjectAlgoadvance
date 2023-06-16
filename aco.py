import random
import  time
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

def aco(cities, iterations, ants, evaporation, alpha, beta, intensification,writer, nbTest, size):
    start_timer=time.time()
    evaporation =evaporation/10
    lastest_best_score = float('inf')
    num_equal=0
    best_serie_counter =0

    pheromone = [[1] * len(cities) for _ in range(len(cities))]

    probability = update(pheromone, alpha, cities, beta)
    available_cities = list(range(len(cities)))

    q = 0

    for i in range(iterations):
        start_iter = time.time()
        start_process_time = time.process_time()
        q+=1
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
        if (best_score < lastest_best_score ) :
            lastest_best_score=best_score
            best_serie_counter += 1

        if(best_score==lastest_best_score):
            num_equal +=1



        for c in range(len(pheromone)):
            for c2 in range(len(pheromone)):
                pheromone[c][c2] *= evaporation

        for z in range(len(best_path_coords[0])):
            pheromone[best_path_coords[0][z]][best_path_coords[1][z]] += intensification

        probability = update(pheromone, alpha, cities, beta)
        process_time = time.process_time() / (i + 1)
        elapsed_time = time.time() - start_iter

    process_time_total = time.process_time() - start_process_time
    time_elapsed_total = time.time() - start_timer
    writer.write(
        "\n" + "test " + str(nbTest) + ":" + ";" + str(elapsed_time) + ";" + str(time_elapsed_total) + ";" + str(
            process_time) + ";" +
        str(process_time_total) + ";" + str(num_equal) + ";" + str(best_score) + ";" + str(
            best_serie_counter) + ";" + str(iterations) + ";" + str(ants) + ";" + str(size) + ";" + str(
            evaporation) + ";"
    )
    if nbTest % 1000 == 0:
        print(time.process_time())

    return best_path_coords, best_path, best_score