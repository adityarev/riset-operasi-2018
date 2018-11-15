from Helpers.UVGenerator import UVGenerator


class CalculatorUVTest:
    @staticmethod
    def run():
        cost = [[8, 6, 10, 9],
                [9, 12, 13, 17],
                [14, 9, 16, 5]]

        distribution = [[15, 30, 0, 0],
                        [30, 0, 30, 0],
                        [0, 0, 10, 40]]

        print('Cost')
        print(cost)

        print('Distribution')
        print(distribution)

        uvg = UVGenerator(cost, distribution)
        uvg.calculate()

        u, v = uvg.get_uv()
        print('\nu', u)
        print('v', v)


def main():
    test = CalculatorUVTest()
    test.run()

if __name__ == '__main__':
    main()
