import random
import time
import numpy as np
import warnings
import networkx as nx
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
outputFile = "./LogTest.txt"

def modifier_premiere_ligne(fichier):
    try:
        with open(fichier, 'x') as file:
            print("fichier créé")
            file.write("1")
            return 1
    except :
        # Ouvrir le fichier en mode lecture et écriture
        with open(fichier, 'r+') as file:
            lignes = file.readlines()  # Lire toutes les lignes du fichier

            if lignes:
                premiere_ligne = lignes[0].strip()  # Récupérer la première ligne
                nb = int(premiere_ligne)
                nb+=1
                del lignes[0]  # Supprimer la première ligne

                # Replacer le curseur au début du fichier
                file.seek(0)

                # Écrire la nouvelle première ligne
                file.write(str(nb)+"\n\n")

                # Écrire les lignes restantes du fichier
                file.writelines(lignes[1:])

                # Tronquer le reste du fichier au cas où les nouvelles lignes sont plus courtes que les anciennes
                file.truncate()


                return nb
            else:
                return None

def adjacency_matrix(matrix):
    timer = time.time()
    adj = np.zeros(matrix.shape)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            adj[i][j] = matrix[i][j]*matrix[j][i]
    print("Runtime adj : ", time.time() - timer)
    return adj

def update(pheromone, alpha, visibility, beta):
    return (pheromone ** alpha) * (visibility ** beta)


def choose_next_city(prob, available, city):
    a = prob[city, available]
    b = np.sum(a)
    p = a/b
    return np.random.choice(range(len(p)), p=p)


def evaluate(matrix, paths):
    scores = np.zeros(len(paths))
    coordinates_i = []
    coordinates_j = []

    for index, path in enumerate(paths):
        score = 0
        coords_i = []
        coords_j = []

        for i in range(len(path) - 1):
            coords_i.append(path[i])
            coords_j.append(path[i + 1])
            score += matrix[path[i], path[i + 1]]
        scores[index] = score
        coordinates_i.append(coords_i)
        coordinates_j.append(coords_j)

    best = np.argmin(scores)

    return (coordinates_i[best], coordinates_j[best]), paths[best], scores[best]


def aoc(matrix, iterations, ants, cities, evaporation, intensification, writer, nbTest):
    writer.write("\n"+"test : "+ str(nbTest))
    start_timer = time.time()
    alpha = 1.0
    beta = 1.0
    # beta_evaporation_rate = 0
    early_stopping_count = 5
    best_score_so_far = 0
    num_equal = 0
    best_series = []
    best_path = 0
    best_serie_counter =0
    counterOn=False

    available_cities = list(range(cities))

    # num_equal = 0

    pheromone = np.ones((cities, cities))
    np.fill_diagonal(pheromone, 0)

    visibility = 1/matrix

    probability = update(pheromone, alpha, visibility, beta)

    for i in range(iterations):
        start_iter = time.time()
        paths = []
        path = []

        for ant in range(ants):
            current_city = 0 #available_cities[0] / set_of_available_nodes[np.random.randint(0, len(self.set_of_available_nodes))] #à surveiller / faut penser qu'il faut revenir au point de départ hein
            path.append(current_city)

            for a in range(len(available_cities), 0, -1):
                available_cities.remove(current_city)
                if len(available_cities) > 0:
                    current_city = available_cities[choose_next_city(probability, available_cities, current_city)]
                    path.append(current_city)

            path.append(0)
            available_cities = list(range(cities))
            paths.append(path)
            path = []

        best_path_coords, best_path, best_score = evaluate(matrix, paths)
        best_serie_counter += 1
        if i == 0:
            best_score_so_far = best_score
        else:
            if best_score < best_score_so_far:
                best_score_so_far = best_score
                best_serie_counter=0

        if best_score == best_score_so_far:
            num_equal += 1
        else:
            num_equal = 0
        print("Process time", time.process_time()/(i+1))
        if best_serie_counter==20 and counterOn==True:
            print("Stopping early due to {} iterations of the same best-score.".format(best_serie_counter),"Nb total iteration {}".format(i))
            break
        print("iteration to stayed the best :", best_serie_counter)


# self.best_series.append(best_score)
        best_series.append(best_score)
        pheromone *= (1 - evaporation)
        # beta *= (1 - beta_evaporation_rate)
        # pheromone[best_path_coords[0], best_path_coords[1]] += intensification
        probability = update(pheromone, alpha, visibility, beta)

        print("Best score at iteration {}: {}; overall: {} elapsed time ({}s)"
              "".format(i, round(best_score, 2), round(best_score_so_far, 2),
                        time.time() - start_iter))

        if best_score == best_score_so_far and num_equal == early_stopping_count:
            print("Stopping early due to {} iterations of the same score.".format(early_stopping_count))
            break

    print("End of iterations in : ", time.time() - start_timer)
    best = best_series[np.argmin(best_series)]
    print("ACO finished. Best score: {}".format(best))
    return best_path

def genGraphique ():
    G = nx.from_numpy_array(m)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    pos = nx.spring_layout(G)

    plt.figure(figsize=(15, 8))

    # Graphe
    plt.subplot(1, 2, 2)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=500, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Graphe')

    # Heatmap
    plt.subplot(1, 2, 1)
    plt.imshow(m, cmap='PuRd', interpolation='nearest')
    plt.colorbar()
    plt.title('Heatmap')

    # Affiche le graphe et la heatmap
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    size =100
    iterations = 20
    grapheOn= False
    # np.fill_diagonal(m, 0)

    # m = adjacency_matrix(m)
    timer = time.time()

    np.random.seed(3)
    m = np.random.random_integers(1, 50, size=(size, size))
    m = (m + m.T)
    np.fill_diagonal(m, 0)

    print("Premier matrice:\n", m)
    print("Runtime : ", time.time() - timer)
    nbTest = modifier_premiere_ligne(outputFile)
    with open(outputFile, 'a') as writer:
        best = aoc(m, iterations=iterations, ants=10, cities=size, evaporation=0.1, intensification=2, writer=writer, nbTest= nbTest)

    print("Best : ", best)
    print("Process : ", time.process_time())
if(grapheOn==True) :
    genGraphique()
