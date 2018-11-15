import copy

from dashtable import data2rst


class ResultTable:
    def __init__(self, source, destination, cost, distribution):
        self.__source = source
        self.__destination = destination
        self.__cost = cost
        self.__distribution = distribution

        self.__spans = []

    # -- Table creator --
    def __new_table(self):
        header = self.__new_header()
        rows = self.__new_rows()

        table = [header]
        for row in rows:
            table.append(row)

        return table

    # -- Header creator --
    def __new_header(self):
        j = 0
        destination = copy.deepcopy(self.__destination)

        header = ['']
        for d in destination:
            header.extend([d, ''])

            # Create header span
            span = self.__new_header_cell_span(j)
            self.__append_spans(span)

            j = j + 1

        return header

    # -- Rows creator --
    def __new_rows(self):
        n = len(self.__source)

        rows = []
        for i in range(n):
            row = self.__new_row(i)
            first_row, second_row = row

            rows.append(first_row)
            rows.append(second_row)

        return rows

    def __new_row(self, i):
        first_row = self.__new_first_row(i)
        second_row = self.__new_second_row(i)

        return first_row, second_row

    def __new_first_row(self, i):
        first_row = [copy.deepcopy(self.__source[i])]

        # Create row label span
        span = self.__new_row_label_cell_span(i)
        self.__append_spans(span)

        distribution = copy.deepcopy(self.__distribution[i])
        for d in distribution:
            first_row.extend([d, ''])

        return first_row

    def __new_second_row(self, i):
        j = 0
        second_row = ['']

        cost = copy.deepcopy(self.__cost[i])
        for c in cost:
            second_row.extend(['%5d' % c, ''])

            # Create distribution and cost span
            spans = self.__new_dist_cost_cell_span(i, j)
            span1, span2 = spans

            self.__append_spans(span1)
            self.__append_spans(span2)

            j = j + 1

        return second_row

    # -- Span creator --
    @staticmethod
    def __new_header_cell_span(j):
        span = [[0, j * 2 + 1], [0, j * 2 + 2]]

        return span

    @staticmethod
    def __new_row_label_cell_span(i):
        span = [[i * 2 + 1, 0], [i * 2 + 2, 0]]

        return span

    @staticmethod
    def __new_dist_cost_cell_span(i, j):
        cell1 = [i * 2 + 1, j * 2 + 1]
        cell2 = [i * 2 + 1, j * 2 + 2]
        cell3 = [i * 2 + 2, j * 2 + 1]
        cell4 = [i * 2 + 2, j * 2 + 2]

        spans = [cell1, cell2], [cell3, cell4]

        return spans

    # -- Modifier methods for private access --
    def __append_spans(self, span):
        spans = copy.deepcopy(self.__spans)

        spans.append(span)
        self.__spans = spans

    # -- Cost list creator --
    def __cost_list(self):
        cells = []
        n_row = len(self.__source)
        n_col = len(self.__destination)

        for i in range(n_row):
            for j in range(n_col):
                dist = copy.deepcopy(self.__distribution[i][j])

                if dist.__ne__(0):
                    cost = copy.deepcopy(self.__cost[i][j])
                    cells.append((dist, cost))

        return cells

    # -- Show methods for private access --
    def __show_table(self):
        table = self.__new_table()
        spans = copy.deepcopy(self.__spans)

        print(data2rst(table, spans))

    def __show_calculation(self):
        cells = self.__cost_list()
        result_str = ''

        ans = 0
        first = True
        while len(cells).__ne__(0):
            if first.__eq__(True):
                first = False
            else:
                result_str += ' + '

            dist, cost = cells.pop(0)
            ans += (dist * cost)

            result_str += '(%d * %d)' % (dist, cost)
        result_str += ' = %d' % ans

        print('\nResult :')
        print(result_str, '\n')

    # -- Show result for public access --
    def show(self, title='Result'):
        print(title)
        self.__show_table()
        self.__show_calculation()
