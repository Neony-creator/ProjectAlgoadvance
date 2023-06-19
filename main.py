import time

import toolbox
import aco

if __name__ == '__main__':

    init1 = toolbox.cpu_memory()
    init2 = toolbox.cpu_usage()

    # iterations = [5, 10, 20, 50, 100]
    # ants = [5, 10, 50, 100, 200, 500, 1000, 2000, 5000]
    # beta = [1, 2, 5, 10, 20]
    # evaporation = [0.1, 0.2, 0.5, 1, 2]
    # intensification = [0.5, 0.8, 1, 1.5, 2, 4]
    # villes = [10, 50, 100, 500, 1000]
    #
    # results = []
    #
    # t = time.time()
    #
    # with open("./LogTest.csv", 'w+') as writer:
    #     for v in villes:
    #         ville = toolbox.generate_cities(v)
    #         for i, a, b, e, inten in itertools.product(iterations, ants, beta, evaporation, intensification):
    #             coords, path, score = aco.aco(ville, i, a, e, 1, b, inten)
    #
    #             writer.write(
    #                 f"{str(v)};{str(i)};{str(a)};{str(b)};{str(e)};{str(inten)};{str(path)};{str(score)};{str(time.time() - t)}"
    #                 + "\n"
    #             )

    # path = [0, 7, 8, 37, 30, 43, 17, 6, 27, 5, 36, 18, 26, 16, 42, 29, 35, 45, 32, 19, 46, 20, 38, 31, 23, 9, 44, 34, 3, 25,
    #  41, 1, 28, 4, 47, 33, 40, 15, 21, 2, 22, 13, 24, 12, 10, 11, 14, 39, 0]
    # path2 = [1,
# 8,
# 38,
# 31,
# 44,
# 18,
# 7,
# 28,
# 6,
# 37,
# 19,
# 27,
# 17,
# 43,
# 30,
# 36,
# 46,
# 33,
# 20,
# 47,
# 21,
# 32,
# 39,
# 48,
# 5,
# 42,
# 24,
# 10,
# 45,
# 35,
# 4,
# 26,
# 2,
# 29,
# 34,
# 41,
# 16,
# 22,
# 3,
# 23,
# 14,
# 25,
# 13,
# 11,
# 12,
# 15,
# 40,
# 9,
# 1]
    # tempa =

    iterations = 10
    ants = 5000
    alpha = 1
    beta = 10
    evaporation = 0.5
    intensification = 0.8
    p = time.process_time()
    t = time.time()

    # v = toolbox.generate_cities(50)
    v = [
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

    # score1 = sum(
    #     toolbox.euclidean_distance(v[path[i]], v[path[i + 1]])
    #     for i in range(len(path)-1)
    # )
    #
    # score2 = sum(
    #     toolbox.euclidean_distance(v[path2[i]], v[path2[i + 1]])
    #     for i in range(len(path)-1)
    # )
    #
    # print("s1 ", score1)
    # print("s2 ", score2)

    print(v)

    paths, scores, means = aco.kcamions(2, v, iterations, ants, evaporation, alpha, beta, intensification)

    for i in range(len(paths)):
        print("Path : ", paths[i])
        print("score : ", scores[i])

    toolbox.afficher_kcamions(means, paths)


    # coords, path, score = aco.aco(v, iterations, ants, evaporation, alpha, beta, intensification)
    #
    # print("Path : ", path)
    # print("coords : ", coords)
    # print("score : ", score)
    #
    # toolbox.afficher(path, v)
    final1 = toolbox.cpu_memory()
    final2 = toolbox.cpu_usage()
    c1 = ((final1 - init1)/1024)/1024
    c2 = final2 - init2
    print("Memory usage : {} Mo".format(c1))
    print("CPU usage : {} %".format(c2))
    print("r1 : ", time.time() - t)
    print("r2 : ", time.process_time() - p)