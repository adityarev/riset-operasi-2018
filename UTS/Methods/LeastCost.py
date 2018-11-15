from Methods.Base.Method import Method
from queue import PriorityQueue


class LeastCost(Method):
    def __init__(self, source, destination, cost, demand, supply):
        super(LeastCost, self).__init__(
            source=source,
            destination=destination,
            cost=cost,
            demand=demand,
            supply=supply
        )

    def calculate(self):
        self._reset_calc()

        pq = self.__priority_queue()

        while not pq.empty():
            _, (i, j) = pq.get()

            if self._calc_taken[i][j].__eq__(0):
                allocated = min(self._calc_supply[i], self._calc_demand[j])
                self._calc_distribution[i][j] = allocated
                self._calc_supply[i] -= allocated
                self._calc_demand[j] -= allocated

                self._cancel_table(i, j)

    def __priority_queue(self):
        pq = PriorityQueue()
        n_source = len(self._source)
        n_destination = len(self._destination)

        for i in range(n_source):
            for j in range(n_destination):
                pq.put((self._cost[i][j], (i, j)))

        return pq
