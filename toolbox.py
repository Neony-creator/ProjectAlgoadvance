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


def kmeans(k, v):
    # means = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(k)]
    # means = [[50, 50] for _ in range(k)]
    points = []
    angles = linspace(0, 2 * math.pi, k + 1)
    for angle in angles:
        x = 100 / 2 * math.cos(angle) + 100 / 2
        y = 100 / 2 * math.sin(angle) + 100 / 2
        points.append((x, y))
    means = [[x, y] for x, y in points]
    print(points)


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
            # for z in range(len(vmeans)):
            #     if vmeans[z] == mean:
            #         count +=1
            #         sommex += v[z][0]
            #         sommey += v[z][1]
            #
            # tx = sommex / count
            # ty = sommey / count
            # means[mean][0] = tx
            # means[mean][1] = ty

    return vmeans

def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i


# def plot_clusters(data, assignments, means):
def plot_clusters(cities, vmeans):
    # num_clusters = len(means)

    # Create a list of colors for each cluster
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'lime']  # Add more colors if needed

    # Plot each data point with its corresponding color
    for i, point in enumerate(cities):
        cluster = vmeans[i]
        color = colors[cluster % len(colors)]  # Assign colors cyclically if there are more clusters than colors
        plt.scatter(point[0], point[1], color=color)

    # for i in range(len(vmeans)):


    # Plot means with larger markers
    # for mean in means:
    #     plt.scatter(mean[0], mean[1], color='black', marker='x', s=100)

    plt.show()