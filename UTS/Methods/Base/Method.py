import copy

from UI.Console.ResultTable import ResultTable


class Method:
    def __init__(self, source, destination, cost, demand, supply):
        self._source = source
        self._destination = destination

        self._cost = cost
        self._demand = demand
        self._supply = supply

        self._calc_distribution = [[]]
        self._calc_demand = [[]]
        self._calc_supply = []
        self._calc_taken = []

    def _cancel_column(self, j):
        n_row = len(self._source)

        for i in range(n_row):
            self._calc_taken[i][j] = 1

    def _cancel_row(self, i):
        n_col = len(self._destination)

        for j in range(n_col):
            self._calc_taken[i][j] = 1

    def _cancel_table(self, i, j):
        if self._calc_supply[i].__eq__(0):
            self._cancel_row(i)
        if self._calc_demand[j].__eq__(0):
            self._cancel_column(j)

    def _reset_calc(self):
        n_source = len(self._source)
        n_destination = len(self._destination)

        self._calc_distribution = [[0 for _ in range(n_destination)] for _ in range(n_source)]
        self._calc_taken = [[0 for _ in range(n_destination)] for _ in range(n_source)]
        self._calc_supply = copy.copy(self._supply)
        self._calc_demand = copy.copy(self._demand)

    def show_ans(self):
        ans = 0
        n_source = len(self._source)
        n_destination = len(self._destination)

        for i in range(n_source):
            for j in range(n_destination):
                ans += self._calc_distribution[i][j] * self._cost[i][j]

        print(ans)

    def _self_copy(self):
        source = copy.copy(self._source)
        destination = copy.copy(self._destination)
        cost = copy.copy(self._cost)
        distribution = copy.copy(self._calc_distribution)

        return source, destination, cost, distribution

    def show_table(self, title):
        self_copy = self._self_copy()
        result_table = ResultTable(*self_copy)

        result_table.show(title)

    # -- Getter methods for public access --
    def get_cost_distribution(self):
        cost = copy.copy(self._cost)
        distribution = copy.copy(self._calc_distribution)

        return cost, distribution
