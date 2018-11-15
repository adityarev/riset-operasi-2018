from UI.Console.ResultTable import ResultTable


class ResultTableTest:
    @staticmethod
    def run():
        source = ['S1', 'S2', 'S3']
        destination = ['D1', 'D2', 'D3', 'D4']
        cost = [[10, 0, 20, 11],
                [12, 7, 9, 20],
                [0, 14, 16, 18]]
        distribution = [[5, 10, 0, 0],
                        [0, 5, 15, 5],
                        [0, 0, 0, 5]]

        res = ResultTable(source, destination, cost, distribution)
        res.show()

def main():
    test = ResultTableTest()
    test.run()

if __name__ == '__main__':
    main()
