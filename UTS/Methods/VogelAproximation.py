import sys

from Methods.Base.Method import Method
from queue import PriorityQueue


class VogelAproximation(Method):
    def __init__(self, source, destination, cost, demand, supply):
        super(VogelAproximation, self).__init__(
            source=source,
            destination=destination,
            cost=cost,
            demand=demand,
            supply=supply
        )

    def __all_transported(self):
        n_source = len(self._source)

        for i in range(n_source):
            if self._calc_supply[i].__ne__(0):
                return 0

        return 1

    def calculate(self):
        self._reset_calc()

        while not self.__all_transported():
            finality = self.__next_finality()
            _, (is_col, ind) = finality.get()
            i, j = self.__minimum_index(is_col, ind)

            allocated = min(self._calc_supply[i], self._calc_demand[j])
            self._calc_distribution[i][j] = allocated
            self._calc_supply[i] -= allocated
            self._calc_demand[j] -= allocated

            self._cancel_table(i, j)

    @staticmethod
    def __diff_return(fir_sec, is_col_ind):
        fir, sec = fir_sec
        is_col, ind = is_col_ind

        if fir.__eq__(sys.maxsize):
            return sys.maxsize, (is_col, ind)
        elif sec.__eq__(sys.maxsize):
            return fir, (is_col, ind)
        else:
            return -abs(fir - sec), (is_col, ind)

    def __diff_col(self, j):
        fir = sys.maxsize
        sec = sys.maxsize
        n_row = len(self._source)

        for i in range(n_row):
            if self._calc_taken[i][j].__eq__(0):
                val = self._cost[i][j]
                if val.__lt__(sec):
                    sec = val
                    if sec.__lt__(fir):
                        fir, sec = sec, fir

        fir_sec = fir, sec
        is_col_ind = 1, j

        return self.__diff_return(fir_sec, is_col_ind)

    def __diff_row(self, i):
        fir = sys.maxsize
        sec = sys.maxsize
        n_col = len(self._destination)

        for j in range(n_col):
            if self._calc_taken[i][j].__eq__(0):
                val = self._cost[i][j]
                if val.__lt__(sec):
                    sec = val
                    if sec.__lt__(fir):
                        fir, sec = sec, fir

        fir_sec = fir, sec
        is_col_ind = 0, i

        return self.__diff_return(fir_sec, is_col_ind)

    def __minimum_index(self, is_col, ind):
        if is_col.__eq__(1):
            return self.__minimum_index_at_col(ind), ind
        else:
            return ind, self.__minimum_index_at_row(ind)

    def __minimum_index_at_col(self, j):
        val = sys.maxsize
        ind = -1
        n_row = len(self._source)

        for i in range(n_row):
            if self._calc_taken[i][j].__eq__(0):
                if self._cost[i][j].__lt__(val):
                    val = self._cost[i][j]
                    ind = i

        return ind

    def __minimum_index_at_row(self, i):
        val = sys.maxsize
        ind = -1
        n_col = len(self._destination)

        for j in range(n_col):
            if self._calc_taken[i][j].__eq__(0):
                if self._cost[i][j].__lt__(val):
                    val = self._cost[i][j]
                    ind = j

        return ind

    def __next_finality(self):
        finality = PriorityQueue()
        n_source = len(self._source)
        n_destination = len(self._destination)

        for i in range(n_source):
            diff = self.__diff_row(i)
            finality.put(diff)

        for j in range(n_destination):
            diff = self.__diff_col(j)
            finality.put(diff)

        return finality
