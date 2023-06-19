import time
import dataset
import held_karp
import toolbox
import aco

if __name__ == '__main__':

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
    ants = 1000
    alpha = 1
    beta = 10
    evaporation = 0.5
    intensification = 0.8
    p = time.process_time()
    t = time.time()

    v = toolbox.generate_cities(10)
    print(v)

    score, path = held_karp.held_karp(v)

    print("Path : ", path)
    print("score : ", score)

    # toolbox.afficher(path, v)

    print("r1 : ", time.time() - t)
    print("r2 : ", time.process_time() - p)

    t = time.time()
    p = time.process_time()

    # v = dataset.dataset1

    # print(v)
    #
    # paths, scores, means = aco.kcamions(10, v, iterations, ants, evaporation, alpha, beta, intensification)
    #
    # for i in range(len(paths)):
    #     print("Path : ", paths[i])
    #     print("score : ", scores[i])
    #
    # toolbox.afficher_kcamions(means, paths)
    #

    coords, path, score = aco.aco(v, iterations, ants, evaporation, alpha, beta, intensification)

    print("Path : ", path)
    print("coords : ", coords)
    print("score : ", score)

    # toolbox.afficher(path, v)

    print("r1 : ", time.time() - t)
    print("r2 : ", time.process_time() - p)