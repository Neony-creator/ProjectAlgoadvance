import time

from matplotlib import pyplot as plt

import toolbox
import sa
import aco

if __name__ == '__main__':

    cities_number = 10
    iterations = 10000
    temperature = 1000000
    cxreduction = 0.70

    p = time.process_time()
    t = time.time()
    nbTest = 0
    outputFile = "./LogTest.txt"



#     v = [
# [6734,1453],
# [2233,810],
# [5530,1424],
# [401,841],
# [3082,1644],
# [7608,4458],
# [7573,3716],
# [7265,1268],
# [6898,1885],
# [1112,2049],
# [5468,2606],
# [5989,2873],
# [4706,2674],
# [4612,2035],
# [6347,2683],
# [6107,669],
# [7611,5184],
# [7462,3590],
# [7732,4723],
# [5900,3561],
# [4483,3369],
# [6101,1110],
# [5199,2182],
# [1633,2809],
# [4307,2322],
# [675,1006],
# [7555,4819],
# [7541,3981],
# [3177,756],
# [7352,4506],
# [7545,2801],
# [3245,3305],
# [6426,3173],
# [4608,1198],
# [23,2216],
# [7248,3779],
# [7762,4595],
# [7392,2244],
# [3484,2829],
# [6271,2135],
# [4985,140],
# [1916,1569],
# [7280,4899],
# [7509,3239],
# [10,2676],
# [6807,2993],
# [5185,3258],
# [3023,1942]]



    #vmeans = toolbox.kmeans(5, v)
    #toolbox.plot_clusters(v, vmeans)

    # cities_coords = toolbox.generate_cities(cities_number)
    cities_coords = [
[6734,1453],
[2233,810],
[5530,1424],
[401,841],
[3082,1644],
[7608,4458],
[7573,3716],
[7265,1268],
[6898,1885],
[1112,2049],
[5468,2606],
[5989,2873],
[4706,2674],
[4612,2035],
[6347,2683],
[6107,669],
[7611,5184],
[7462,3590],
[7732,4723],
[5900,3561],
[4483,3369],
[6101,1110],
[5199,2182],
[1633,2809],
[4307,2322],
[675,1006],
[7555,4819],
[7541,3981],
[3177,756],
[7352,4506],
[7545,2801],
[3245,3305],
[6426,3173],
[4608,1198],
[23,2216],
[7248,3779],
[7762,4595],
[7392,2244],
[3484,2829],
[6271,2135],
[4985,140],
[1916,1569],
[7280,4899],
[7509,3239],
[10,2676],
[6807,2993],
[5185,3258],
[3023,1942]]

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first, second in zip(cities_coords[:-1], cities_coords[1:]):
        ax1.plot([first[0], second[0]], [first[1], second[1]], 'b')
    ax1.plot([cities_coords[0][0], cities_coords[-1][0]], [cities_coords[0][1], cities_coords[-1][1]], 'b')
    for c in cities_coords:
        ax1.plot(c[0], c[1], 'ro')

    print(sa.distance_total(cities_coords))
    result, cities_coords = sa.sa(temperature, cxreduction, iterations, cities_coords)
    print(result)
    for first, second in zip(cities_coords[:-1], cities_coords[1:]):
        ax2.plot([first[0], second[0]], [first[1], second[1]], 'b')
    ax2.plot([cities_coords[0][0], cities_coords[-1][0]], [cities_coords[0][1], cities_coords[-1][1]], 'b')
    for c in cities_coords:
        ax2.plot(c[0], c[1], 'ro')
    plt.show()



    # print("Path : ", path)
    # print("coords : ", coords)
    # print("score : ", score)
    #
    # toolbox.afficher(path, v)

    print("r1 : ", time.time() - t)
    print("r2 : ", time.process_time() - p)