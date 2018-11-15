from UI.GUI.Input import Input


class InputTest:
    @staticmethod
    def run():
        source = ['1', '2', '3']
        destination = ['A', 'B', 'C', 'D']

        inp = Input(source, destination)
        inp.run()


def main():
    test = InputTest()
    test.run()


if __name__ == '__main__':
    main()