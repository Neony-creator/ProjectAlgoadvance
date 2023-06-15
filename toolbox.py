import math
import random
import numpy as np


def generate_cities(n):
    return [[random.randint(1, 100), random.randint(1, 100)] for _ in range(n)]

# def generate_matrix(n):
    # m = np.random.random_integers(1, 100, size=(n, n))
    # msymm = m + m.T
    # return np.fill_diagonal(msymm, 0)

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

