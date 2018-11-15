from Methods.Base.Method import Method


class NorthwestCorner(Method):
    def __init__(self, source, destination, cost, demand, supply):
        super(NorthwestCorner, self).__init__(
            source=source,
            destination=destination,
            cost=cost,
            demand=demand,
            supply=supply
        )

    def calculate(self):
        self._reset_calc()

        n = 0
        w = 0
        n_source = len(self._source)
        n_destination = len(self._destination)

        while n.__lt__(n_source) and w.__lt__(n_destination):
            allocated = min(self._calc_supply[n], self._calc_demand[w])
            self._calc_distribution[n][w] = allocated
            self._calc_supply[n] -= allocated
            self._calc_demand[w] -= allocated

            self._cancel_table(n, w)
            n, w = self.__new_nw(n, w)

    def __new_nw(self, n, w):
        new_n = n
        new_w = w

        if self._calc_supply[n].__eq__(0):
            new_n = n + 1
        if self._calc_demand[w].__eq__(0):
            new_w = w + 1

        return new_n, new_w
