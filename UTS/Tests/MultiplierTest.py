from Methods.Multiplier import Multiplier


class MultiplierTest:
    @staticmethod
    def run():
        cost = [[3, 1, 7, 4],
                [2, 6, 5, 9],
                [8, 3, 3, 2]]
        # cost = [[10, 0, 20, 11],
        #         [12, 7, 9, 20],
        #         [0, 14, 16, 18]]

        distribution = [[250, 50, 0, 0],
                        [0, 300, 100, 0],
                        [0, 0, 300, 200]]
        # distribution = [[5, 10, 0, 0],
        #                 [0, 5, 15, 5],
        #                 [0, 0, 0, 5]]

        m = Multiplier(cost, distribution)
        m.calculate()
        m.show_ans()


def main():
    test = MultiplierTest()
    test.run()

if __name__ == '__main__':
    main()
