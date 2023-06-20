import toolbox

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