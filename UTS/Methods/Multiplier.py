import copy
import sys
import os

from queue import PriorityQueue
from Helpers.UVGenerator import UVGenerator
from Helpers.Map import Map


class Multiplier:
    def __init__(self, cost, distribution):
        self.__cost = cost
        self.__distribution = distribution

        n_u = len(cost)
        n_v = len(cost[0])

        self.__u = ['NaN' for _ in range(n_u)]
        self.__v = ['NaN' for _ in range(n_v)]

        self.__iter = 0

    # -- Main action --
    def calculate(self):
        proceed_ok = self.__proceed_status()

        if proceed_ok.__eq__(True):
            self.__run_calculate()
        else:
            print("ERROR! Can't proceed multiplier optimization, number_of(distribution)",
                  "not equal to (number_of(source) + number_of(destination) - 1)\n",
                  "Probably this is the optimum distribution :)\n")

    def __run_calculate(self):
        while True:
            self.__modify_uv()

            nbv = self.__nbv_priority_queue()
            nbv_max = nbv.get()

            min_val, (i, j) = nbv_max
            max_val = -min_val          # reverse value, because in queue, we save the -val
            optimum = self.__optimum_status(max_val)

            if optimum.__eq__(True):
                break

            point = i, j
            d_point = self.__diagonal_point(point)

            while not nbv.empty():
                d_x, d_y = d_point

                if d_x.__ne__(sys.maxsize) and d_y.__ne__(sys.maxsize):
                    break

                _, point = nbv.get()
                d_point = self.__diagonal_point(point)

            self.__modify_distribution(point)

    # -- Optimum checker --
    @staticmethod
    def __optimum_status(max_val):
        return max_val.__lt__(0)

    # -- Process validator --
    def __allocated_count(self):
        m = len(self.__u)
        n = len(self.__v)
        counter = 0

        for i in range(m):
            for j in range(n):
                if self.__distribution[i][j].__ne__(0):
                    counter += 1

        return counter

    def __proceed_status(self):
        m = len(self.__u)
        n = len(self.__v)
        count = self.__allocated_count()

        return count.__eq__(m + n - 1)

    # -- Modifier --
    def __update_iteration(self):
        self.__iter += 1

    def __modify_uv(self):
        cost = copy.deepcopy(self.__cost)
        distribution = copy.deepcopy(self.__distribution)

        iteration = self.__iter
        print("Distribution %d" % iteration, distribution, '\n')
        self.__update_iteration()

        uvg = UVGenerator(cost, distribution)
        uvg.calculate()

        u, v = uvg.get_uv()
        self.__set_uv(u, v)

    def __modify_distribution(self, point):
        map_ = Map(copy.deepcopy(self.__distribution))

        x, y = point
        map_.set_xy(x, y)
        d_x, d_y = map_.diagonal_point()

        distribution = copy.deepcopy(self.__distribution)
        allocated = min(distribution[x][d_y], distribution[d_x][y])

        # decrease cross side diagonal line
        distribution[x][d_y] -= allocated
        distribution[d_x][y] -= allocated

        # increase diagonal line
        distribution[x][y] += allocated
        distribution[d_x][d_y] += allocated

        self.__set_distribution(distribution)

    # -- Diagonal point finder --
    def __diagonal_point(self, point):
        x, y = point
        map_ = Map(copy.deepcopy(self.__distribution))
        map_.set_xy(x, y)

        return map_.diagonal_point()

    # -- Non Basic Variables (NBV) handler --
    def __nbv_priority_queue(self):
        nbv = PriorityQueue()
        n_u = len(self.__cost)
        n_v = len(self.__cost[0])

        for i in range(n_u):
            for j in range(n_v):
                if self.__distribution[i][j].__eq__(0):
                    val = self.__u[i] + self.__v[j] - self.__cost[i][j]

                    nbv.put((-val, (i, j)))

        return nbv

    # -- Setter methods for private access
    def __set_uv(self, u, v):
        self.__u, self.__v = u, v

    def __set_distribution(self, distribution):
        self.__distribution = distribution

    # -- Viewer method for public access --
    def show_ans(self):
        ans = 0
        n_u = len(self.__cost)
        n_v = len(self.__cost[0])

        for i in range(n_u):
            for j in range(n_v):
                ans += self.__cost[i][j] * self.__distribution[i][j]

        print(ans)

    # -- Getter methods for public access --
    def get_cost_distribution(self):
        cost = copy.copy(self.__cost)
        distribution = copy.copy(self.__distribution)

        return cost, distribution
