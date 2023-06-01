import random
import time


class Ville:
    def __init__(self, nomSimple):
        self.nomSimple = nomSimple
        self.voisins = []
        self.distances = []

    def __str__(self):
        toReturn = [v.nomSimple + "," + str(d) + "," for v, d in zip(self.voisins, self.distances)]
        return self.nomSimple + "," + "".join(toReturn)


def main():
    temp = []
    a = 2
    for h in range(1, a):
        start_time = time.time()

        filename = "./villes_france_mini.csv"
        output = "./villes_et_voisins"

        villes = []

        with open(filename, 'r') as reader:
            for line in reader:
                nom = line.split(',')[3].replace("\"", "")
                v = Ville(nom)
                villes.append(v)

        random.seed()
        villesFinales = []
        boucles = len(villes)

        for _ in range(boucles):
            current = random.randint(0, len(villes) - 1)
            v = villes.pop(current)
            villesFinales.append(v)

            if len(villes) > 0:
                nbVoisins = random.randint(1, 3)
                for _ in range(nbVoisins):
                    voisin = random.choice(villes)

                    if voisin not in v.voisins:
                        d = random.randint(2, 99)
                        v.voisins.append(voisin)
                        v.distances.append(d)
                        voisin.voisins.append(v)
                        voisin.distances.append(d)

        with open(output, 'w') as writer:
            for ville in villesFinales:
                writer.write(str(ville) + "\n")

        # print(str(h), "Runtime: ", time.process_time()/h)
        end_time = time.time()
        runtime = end_time - start_time
        # print(str(h), "Runtime :" + str(runtime))
        temp.append(runtime)

    print("Runtime 1 :" + str(time.process_time() / a))
    print("Runtime 2 :" + str(sum(x for x in temp) / a))


if __name__ == '__main__':
    main()
