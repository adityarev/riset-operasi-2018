import copy

from Methods.LeastCost import LeastCost
from Methods.NorthwestCorner import NorthwestCorner
from Methods.VogelAproximation import VogelAproximation
from Methods.Multiplier import Multiplier
from UI.Console.InputTable import InputTable
from UI.Console.ResultTable import ResultTable
from UI.GUI.Input import Input


class Main:
    def __init__(self):
        self.__source = ['1', '2', '3']
        self.__destination = ['A', 'B', 'C', 'D']

        self.__cost = [[3, 1, 7, 4],
                       [2, 6, 5, 9],
                       [8, 3, 3, 2]]
        self.__supply = [300, 400, 500]
        self.__demand = [250, 350, 400, 200]

    # -- Main run --
    def run(self):
        self.__run_input()

        self_copy = self.__self_copy()
        table = InputTable(*self_copy)

        table.show()
        self.__show_instruction()

        while True:
            try:
                inp = int(input('>>> '))

                if inp.__eq__(0):
                    self.__run_exit()
                    print('Bye. . .')
                    break
                else:
                    self.__run_action(inp)

            except ValueError:
                print('Error input!!\n')
                continue

    # -- Input runner method --
    def __run_input(self):
        source = copy.deepcopy(self.__source)
        destination = copy.deepcopy(self.__destination)

        inp = Input(source, destination)
        inp.run()

        cost = inp.get_cost()
        self.__set_cost(cost)

        supply = inp.get_supply()
        self.__set_supply(supply)

        demand = inp.get_demand()
        self.__set_demand(demand)

    def __run_exit(self):
        self.__show_exit_instruction()

        while True:
            try:
                inp = int(input('>>> '))

                if inp.__ge__(1) and inp.__le__(3):
                    self.__run_mul(inp)
                    break
                else:
                    print('Wrong command!!!\n')

            except ValueError:
                print('Error input!!\n')
                continue

    # -- Instruction UI --
    @staticmethod
    def __show_instruction():
        display = ['Command solve list:',
                   '1. North West Corner Method',
                   '2. Least Cost Method',
                   '3. Vogel Aproximation Method',
                   '',
                   '- 0. Exit -\n']

        for d in display:
            print(d)

    @staticmethod
    def __show_exit_instruction():
        print('\nChoose method that you want to fix and find the',
              'optimum configuration with Multiplier Method (1/2/3)')

    # -- Input action --
    def __run_action(self, inp):
        if inp.__eq__(1):
            self.__run_nw()
        elif inp.__eq__(2):
            self.__run_lc()
        elif inp.__eq__(3):
            self.__run_voa()
        else:
            print('Wrong command!!!\n')

    # -- Run result methods --
    def __run_lc(self):
        self_copy = self.__self_copy()
        lc = LeastCost(*self_copy)

        lc.calculate()
        lc.show_table('Least Cost Method')

    def __run_nw(self):
        self_copy = self.__self_copy()
        nw = NorthwestCorner(*self_copy)

        nw.calculate()
        nw.show_table('North West Method')

    def __run_voa(self):
        self_copy = self.__self_copy()
        voa = VogelAproximation(*self_copy)

        voa.calculate()
        voa.show_table('Vogel Aproximation Method')

    def __run_mul(self, inp):
        cost, distribution = self.__init_mul_cost_distribution(inp)
        self_copy = self.__self_multiplier_copy(cost, distribution)

        result_table = ResultTable(*self_copy)
        result_table.show('Multiplier Method')

    # -- Calculator methods --
    def __init_mul_cost_distribution(self, inp):
        self_copy = self.__self_copy()
        cost, distribution = [[]], [[]]

        if inp.__eq__(1):
            nw = NorthwestCorner(*self_copy)
            nw.calculate()

            cost, distribution = nw.get_cost_distribution()
        elif inp.__eq__(2):
            lc = LeastCost(*self_copy)
            lc.calculate()

            cost, distribution = lc.get_cost_distribution()
        elif inp.__eq__(3):
            voa = VogelAproximation(*self_copy)
            voa.calculate()

            cost, distribution = voa.get_cost_distribution()

        return cost, distribution

    # -- Duplicate methods --
    def __self_copy(self):
        source = copy.copy(self.__source)
        destination = copy.copy(self.__destination)
        cost = copy.copy(self.__cost)
        demand = copy.copy(self.__demand)
        supply = copy.copy(self.__supply)

        return source, destination, cost, demand, supply

    def __self_multiplier_copy(self, cost, distribution):
        m = Multiplier(cost, distribution)
        m.calculate()

        m_cost, m_distribution = m.get_cost_distribution()
        source = copy.copy(self.__source)
        destination = copy.copy(self.__destination)

        return source, destination, m_cost, m_distribution

    # -- Setter methods to update private attribute --
    def __set_cost(self, cost):
        self.__cost = cost

    def __set_supply(self, supply):
        self.__supply = supply

    def __set_demand(self, demand):
        self.__demand = demand


if __name__ == '__main__':
    main = Main()
    main.run()
