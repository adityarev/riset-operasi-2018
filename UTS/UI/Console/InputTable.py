import copy

from terminaltables import AsciiTable


class InputTable:
    def __init__(self, source, destination, cost, demand, supply):
        self.__source = source
        self.__destination = destination
        self.__cost = cost
        self.__demand = demand
        self.__supply = supply

    # -- Table data creator --
    def __new_table_data(self):
        header = self.__new_header()
        rows = self.__new_rows()
        footer = self.__new_footer()

        table_data = [header]
        for row in rows:
            table_data.append(row)
        table_data.append(footer)

        return table_data

    # -- Header creator --
    def __new_header(self):
        header = ['']
        header.extend(copy.deepcopy(self.__destination))
        header.extend(['Supply'])

        return header

    # -- Rows creator --
    def __new_rows(self):
        rows = []
        n = len(self.__source)

        for i in range(n):
            row = self.__new_row(i)
            rows.append(row)

        return rows

    def __new_row(self, i):
        row = [copy.copy(self.__source[i])]
        row.extend(copy.copy(self.__cost[i]))
        row.append(copy.copy(self.__supply[i]))

        return row

    # -- Footer creator --
    def __new_footer(self):
        footer = ['Demand']
        footer.extend(copy.copy(self.__demand))
        footer.extend([''])

        return footer

    # -- Show table for public access --
    def show(self):
        table_data = self.__new_table_data()
        table = AsciiTable(table_data)

        print(table.table)
        print('')
