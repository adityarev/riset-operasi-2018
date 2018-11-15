class UVGenerator:
    def __init__(self, cost, distribution):
        self.__cost = cost
        self.__distribution = distribution

        n_u = len(cost)
        n_v = len(cost[0])

        self.__u = ['NaN' for _ in range(n_u)]
        self.__v = ['NaN' for _ in range(n_v)]

    # -- Basic Variables (BV) handler --
    def __basic_variable_list(self):
        bv = []
        n_row = len(self.__cost)
        n_col = len(self.__cost[0])

        for i in range(n_row):
            for j in range(n_col):
                if self.__distribution[i][j].__ne__(0):
                    bv.append((self.__cost[i][j], (i, j)))

        return bv

    # -- UV Modifier --
    def __new_u(self):
        n_u = len(self.__cost)
        return ['NaN' for _ in range(n_u)]

    def __new_v(self):
        n_v = len(self.__cost[0])
        return ['NaN' for _ in range(n_v)]

    def calculate(self):
        bv = self.__basic_variable_list()
        u = self.__new_u()
        v = self.__new_v()

        u[0] = 0
        while len(bv).__ne__(0):
            # print('euy')

            val, (i, j) = bv.pop(0)

            if u[i] == 'NaN' and v[j] == 'NaN':
                bv.append((val, (i, j)))
            elif u[i] == 'NaN':
                u[i] = val - v[j]
            elif v[j] == 'NaN':
                v[j] = val - u[i]
            else:
                continue

        self.__set_uv(u, v)

    # -- Setter methods for private access --
    def __set_uv(self, u, v):
        self.__u = u
        self.__v = v

    # -- Setter methods for public access --
    def set_distribution(self, distribution):
        self.__distribution = distribution

    # -- Getter methods for public access --
    def get_uv(self):
        return self.__u, self.__v
