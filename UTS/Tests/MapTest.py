from Helpers.Map import Map


class MapTest:
    @staticmethod
    def run():
        distribution = [[15, 30, 0, 0],
                        [30, 0, 30, 0],
                        [0, 0, 10, 40]]

        map_ = Map(distribution)
        map_.set_xy(0, 2)
        d = map_.diagonal_point()

        print('(0, 2)')
        map_.view_map()
        print(d, '\n')

        distribution = [[0, 30, 15, 0],
                        [45, 0, 15, 0],
                        [0, 0, 10, 40]]

        map_ = Map(distribution)
        map_.set_xy(2, 1)
        d = map_.diagonal_point()

        print('(2, 1)')
        map_.view_map()
        print(d)


def main():
    test = MapTest()
    test.run()

if __name__ == '__main__':
    main()
