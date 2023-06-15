import math
import random
import matplotlib.pyplot as plt


def generate_cities(n):
    return [[random.randint(1, 100), random.randint(1, 100)] for _ in range(n)]


def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def afficher(path, cities):
    fig, ax = plt.subplots()

    ax.scatter([city[0] for city in cities], [city[1] for city in cities], color='blue', zorder=2)

    for i, city in enumerate(cities):
        if i == path[0]:
            ax.scatter(city[0], city[1], color='red', marker='s', s=100)
        else:
            ax.scatter(city[0], city[1], color='blue')

    for i in range(len(path) - 1):
        start = cities[path[i]]
        end = cities[path[i + 1]]
        ax.plot([start[0], end[0]], [start[1], end[1]], color='black')

    ax.grid(False)

    plt.show()