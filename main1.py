import numpy
import matplotlib.pyplot as plt
import random


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a, b):
        return numpy.sqrt(numpy.abs(a.x - b.x)**2 + numpy.abs((a.y - b.y)**2))

    @staticmethod
    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:-1], coords[1:]):
            dist += Coordinate.get_distance(first, second)
        dist += Coordinate.get_distance(coords[0], coords[-1])
        return dist



if __name__ == '__main__':
    # Fill up the coordinates
    coords = []
    test = [
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
    for i in test:
        coords.append(Coordinate(i[0], i[1]))
    print(coords)
    # machin = [1, 5, 20]
    # for i in machin
    # Plot

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first, second in zip(coords[:-1], coords[1:]):
        ax1.plot([first.x, second.x], [first.y, second.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')



    # Simulated annealing algorithm
    cost0 =Coordinate.get_total_distance(coords)

    T = 10000
    factor = 0.5
    T_init =T

    for i in range(50000):
        #print(i, 'cost =', cost0)
        if T>0.001:
            T = T*factor

        # Exchange two coordinates and get a new neighbour solution
        r1, r2 = numpy.random.randint(0, len(coords), size=2)

        temp =coords[r1]
        coords[r1] =coords[r2]
        coords[r2] = temp

        # Get the new cost
        cost1 = Coordinate.get_total_distance(coords)

        if cost1 < cost0:
            cost0=cost1
        else:
            x = numpy.random.uniform()
            if x < numpy.exp((cost0-cost1)/T):
                cost0=cost1
            else:
                temp = coords[r1]
                coords[r1] = coords[r2]
                coords[r2] = temp
    coords.append(coords[0])
    # Plot th result


    for first, second in zip(coords[:-1], coords[1:]):
        ax2.plot([first.x, second.x], [first.y, second.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x, c.y, 'ro')

    plt.show()

    print( 'cost =', cost0)
