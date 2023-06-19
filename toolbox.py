import math
import random
from collections import defaultdict
import psutil
import os

import matplotlib.pyplot as plt

def generate_cities(n):
    return [[random.randint(1, 100), random.randint(1, 100)] for _ in range(n)]


def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def afficher(path, cities):

    plt.scatter([city[0] for city in cities], [city[1] for city in cities], color='blue', zorder=2)

    for i, city in enumerate(cities):
        if i == path[0]:
            plt.scatter(city[0], city[1], color='red', marker='s', s=100)
        else:
            plt.scatter(city[0], city[1], color='blue')

    for i in range(len(path) - 1):
        start = cities[path[i]]
        end = cities[path[i + 1]]
        plt.plot([start[0], end[0]], [start[1], end[1]], color='black')

    plt.grid(False)
    plt.figure(figsize=(16, 9))
    plt.show()


def pie(k, v):
    points = []
    angles = linspace(0, 2 * math.pi, k + 1)
    for angle in angles:
        x = 100 / 2 * math.cos(angle) + 100 / 2
        y = 100 / 2 * math.sin(angle) + 100 / 2
        points.append((x, y))
    means = [[x, y] for x, y in points]

    vmeans = []

    for _ in range(1):
        for j in range(len(v)):
            distance = [euclidean_distance(means[z], v[j]) for z in range(k)]
            a = min(distance)
            mean = distance.index(a)
            vmeans.append(mean)

    return vmeans

def kmeans(k, v):
    # means = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(k)]
    means = [[v[0][0], v[0][1]] for _ in range(k)]



    vmeans = []

    for _ in range(1):
        for j in range(len(v)):
            distance = [euclidean_distance(means[z], v[j]) for z in range(k)]
            a = min(distance)
            mean = distance.index(a)
            vmeans.append(mean)

            sommex = 0
            sommey = 0
            count = 0
            for z in range(len(vmeans)):
                if vmeans[z] == mean:
                    count +=1
                    sommex += v[z][0]
                    sommey += v[z][1]

            tx = sommex / count
            ty = sommey / count
            means[mean][0] = tx
            means[mean][1] = ty

    return vmeans

def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

def afficher_kcamions(clusters, paths):

    colors = ['lightsalmon', 'lime', 'royalblue', 'lavender', 'crimson', 'fuchsia', 'red', 'green', 'orange', 'purple', 'yellow',]

    for i, cluster in enumerate(clusters):
        cluster_color = colors[i % len(colors)]
        x = [coord[0] for coord in [cluster[point] for point in paths[i]]]
        y = [coord[1] for coord in [cluster[point] for point in paths[i]]]
        plt.plot(x, y, color=cluster_color)

        x = [coord[0] for coord in cluster]
        y = [coord[1] for coord in cluster]
        plt.scatter(x[1:], y[1:], color=cluster_color)  # Plot cities excluding the first city
        plt.scatter(x[0], y[0], color='blue', marker='s', zorder=3)

    plt.show()


def get_sublists(lst):
    sublists = defaultdict(list)
    for i, num in enumerate(lst):
        sublists[num].append(i)
    return list(sublists.values())


def cpu_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def cpu_pro():
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
    return sum(cpu_percentages) / len(cpu_percentages)

