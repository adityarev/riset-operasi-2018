import sys


class Map:
    def __init__(self, distribution):
        self.__x = 0
        self.__y = 0

        self.__row = len(distribution)
        self.__col = len(distribution[0])

        self.__map = self.__init_map(distribution)
        self.__exp = [[(0, 0) for _ in range(2)] for _ in range(2)]  # expansion matrix

    def __build_exp(self):
        x = self.__x
        y = self.__y

        temp = self.__map[x][y]
        self.__map[x][y] = 1
        self.__set_exp()
        self.__map[x][y] = temp

    def diagonal_point(self):
        x = self.__x
        y = self.__y
        x_ = sys.maxsize
        y_ = sys.maxsize
        dist = self.__manhattan_distance((x, y), (x_, y_))

        self.__build_exp()
        for i in range(2):
            for j in range(2):
                d_x, d_y = self.__exp[i][j]
                d_dist = self.__manhattan_distance((x, y), (d_x, d_y))

                if d_dist.__lt__(dist):
                    dist = d_dist
                    x_ = d_x
                    y_ = d_y

        return x_, y_

    def __is_square(self, top_left, bottom_right):
        t, l = top_left
        b, r = bottom_right

        return (
            True
            and self.__map[t][l].__eq__(1)
            and self.__map[t][r].__eq__(1)
            and self.__map[b][l].__eq__(1)
            and self.__map[b][r].__eq__(1)
        )

    @staticmethod
    def __manhattan_distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def __init_map(distribution):
        map_ = distribution
        m = len(distribution)
        n = len(distribution[0])

        for i in range(m):
            for j in range(n):
                if map_[i][j].__gt__(0):
                    map_[i][j] = 1

        return map_

    def __ne_point(self, x, y):
        for i in range(x - 1, -1, -1):
            for j in range(y + 1, self.__col, 1):
                top_left = min(x, i), min(y, j)
                bottom_right = max(x, i), max(y, j)

                if self.__is_square(top_left, bottom_right):
                    return i, j

        return sys.maxsize, sys.maxsize

    def __nw_point(self, x, y):
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                top_left = min(x, i), min(y, j)
                bottom_right = max(x, i), max(y, j)

                if self.__is_square(top_left, bottom_right):
                    return i, j

        return sys.maxsize, sys.maxsize

    def __se_point(self, x, y):
        for i in range(x + 1, self.__row, 1):
            for j in range(y + 1, self.__col, 1):
                top_left = min(x, i), min(y, j)
                bottom_right = max(x, i), max(y, j)

                if self.__is_square(top_left, bottom_right):
                    return i, j

        return sys.maxsize, sys.maxsize

    def __sw_point(self, x, y):
        for i in range(x + 1, self.__row, 1):
            for j in range(y - 1, -1, -1):
                top_left = min(x, i), min(y, j)
                bottom_right = max(x, i), max(y, j)

                if self.__is_square(top_left, bottom_right):
                    return i, j

        return sys.maxsize, sys.maxsize

    def __set_exp(self):
        x = self.__x
        y = self.__y

        self.__exp[0][0] = self.__nw_point(x, y)
        self.__exp[0][1] = self.__ne_point(x, y)
        self.__exp[1][0] = self.__sw_point(x, y)
        self.__exp[1][1] = self.__se_point(x, y)

    def set_xy(self, x, y):
        self.__x = x
        self.__y = y

    def view_map(self):
        print(self.__map)
