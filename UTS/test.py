import copy

from Methods.LeastCost import LeastCost
from Methods.NorthwestCorner import NorthwestCorner
from Methods.VogelAproximation import VogelAproximation
from UI.Console.InputTable import InputTable
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

    def __check_self(self):
        print(self.__cost)
        print(self.__supply)
        print(self.__demand)

    # -- Main run --
    def run(self):
        self.run_input()

        self_copy = self.__self_copy()
        table = InputTable(*self_copy)

        table.show()
        self.__show_instruction()

        while True:
            try:
                inp = int(input('>>> '))

                if inp.__eq__(0):
                    print('Exit. . .')
                    break
                else:
                    self.__run_action(inp)

            except ValueError:
                print('Error input!!\n')
                continue

    # -- Input runner method --
    def run_input(self):
        source = copy.deepcopy(self.__source)
        destination = copy.deepcopy(self.__destination)

        inp = Input(source, destination)
        inp.run()

        cost = inp.get_cost()
        print(cost)
        self.__set_cost(cost)

        supply = inp.get_supply()
        print(supply)
        self.__set_supply(supply)

        demand = inp.get_demand()
        print(demand)
        self.__set_demand(demand)

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

    # -- Duplicate method to get all private attribute value --
    def __self_copy(self):
        source = copy.copy(self.__source)
        destination = copy.copy(self.__destination)
        cost = copy.copy(self.__cost)
        demand = copy.copy(self.__demand)
        supply = copy.copy(self.__supply)

        return source, destination, cost, demand, supply

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
