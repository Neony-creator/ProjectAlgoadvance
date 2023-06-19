import random
import time
import dataset
import held_karp
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

    iterations = 10
    ants = 5
    alpha = 1
    beta = 10
    evaporation = 0.5
    intensification = 0.8
    p = time.process_time()
    t = time.time()

    v = toolbox.generate_cities(10)
    # v = dataset.dataset1
    # print(v)

    # score, path = held_karp.held_karp(v)

    # print("Path : ", path)
    # print("score : ", score)


    # coords, path, score = aco.aco(v, iterations, ants, evaporation, alpha, beta, intensification)
    #
    # print("Path : ", path)
    # print("coords : ", coords)
    # print("score : ", score)
    #
    # toolbox.afficher(path, v)

    # print("r1 : ", time.time() - t)
    # print("r2 : ", time.process_time() - p)
    #
    # t = time.time()
    # p = time.process_time()

    # v = dataset.dataset1

    print(v)
    #
    paths, scores, means = aco.kcamions(3, v, iterations, ants, evaporation, alpha, beta, intensification, True)

    for i in range(len(paths)):
        print("Path : ", paths[i])
        print("score : ", scores[i])

    toolbox.afficher_kcamions(means, paths)

    paths, scores, means = aco.kcamions(3, v, iterations, ants, evaporation, alpha, beta, intensification, False)

    for i in range(len(paths)):
        print("Path : ", paths[i])
        print("score : ", scores[i])

    toolbox.afficher_kcamions(means, paths)


    path, score = aco.aco(v, iterations, ants, evaporation, alpha, beta, intensification)

    print("Path : ", path)
    print("score : ", score)

    toolbox.afficher(path, v)

    final1 = toolbox.cpu_memory()
    final2 = toolbox.cpu_usage()
    c1 = ((final1 - init1)/1024)/1024
    c2 = final2 - init2
    print("Memory usage : {} Mo".format(c1))
    print("CPU usage : {} %".format(c2))
    print("r1 : ", time.time() - t)
    print("r2 : ", time.process_time() - p)