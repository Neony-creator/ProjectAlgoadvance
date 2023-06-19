import itertools
import sys

import toolbox


def find_optimal_path(dp, distances, subset):
    n = len(subset)
    path = [0]
    last = 0
    for _ in range(n - 1):
        min_distance = sys.maxsize
        next_city = None
        for j in subset:
            if j == 0:
                continue
            if dp[(subset, j)] + distances[j][last] < min_distance:
                min_distance = dp[(subset, j)] + distances[j][last]
                next_city = j
        path.append(next_city)
        subset = tuple(x for x in subset if x != next_city)
        last = next_city
    path.append(0)
    return path


def held_karp(cities):
    n = len(cities)
    memo = {}

    def tsp(mask, pos):
        if (mask, pos) in memo:
            return memo[(mask, pos)]

        if mask == (1 << n) - 1:
            return toolbox.euclidean_distance(cities[pos], cities[0]), [pos, 0]

        ans = float('inf')
        path = []
        for nxt in range(n):
            if (mask >> nxt) & 1 == 0:
                cost, subpath = tsp(mask | (1 << nxt), nxt)
                cost += toolbox.euclidean_distance(cities[pos], cities[nxt])
                if cost < ans:
                    ans = cost
                    path = [pos] + subpath

        memo[(mask, pos)] = ans, path
        return ans, path
    return tsp(1, 0)