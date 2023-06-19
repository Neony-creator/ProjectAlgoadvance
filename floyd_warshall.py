import itertools

import toolbox


def fw(cities):

    num_cities = len(cities)

    distances = [[toolbox.euclidean_distance(cities[i], cities[j])
                  for j in range(num_cities)]
                for i in range(num_cities)]

    print(distances)

    dp = distances[:]

    path = [[None] * num_cities for _ in range(num_cities)]
    for i, j in itertools.product(range(num_cities), range(num_cities)):
        path[i][j] = j

    for k, i, j in itertools.product(range(num_cities), range(num_cities), range(num_cities)):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    min_distance = float('inf')
    optimal_route = []

    for start_city in range(num_cities):
        visited = [False] * num_cities
        current_city = start_city
        tsp_route = [current_city]
        total_distance = 0

        while len(tsp_route) < num_cities:
            visited[current_city] = True
            next_city = None
            min_next_distance = float('inf')

            for neighbor_city in range(num_cities):
                if not visited[neighbor_city] and dp[current_city][neighbor_city] < min_next_distance:
                    next_city = neighbor_city
                    min_next_distance = dp[current_city][neighbor_city]

            tsp_route.append(next_city)
            total_distance += min_next_distance
            current_city = next_city

        total_distance += dp[current_city][start_city]

        if total_distance < min_distance:
            min_distance = total_distance
            optimal_route = tsp_route

    optimal_route.append(optimal_route[0])
    return min_distance, optimal_route