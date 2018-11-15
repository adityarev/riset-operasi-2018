import copy

from tkinter import *


class Input:
    def __init__(self, source, destination):
        self.__source = source
        self.__destination = destination
        self.__widget = Tk()

        self.__rows = []

    def run(self):
        header_label = self.__new_header_label()
        rows_label = self.__new_rows_label()

        self.__set_widget_grid(header_label, rows_label)
        Button(self.__widget, text='Submit', command=self.on_ok_button_pressed) \
            .grid(row=len(rows_label), column=len(header_label) - 1, sticky=SE, pady=4, padx=4)

        mainloop()

    # -- Label creator --
    def __new_header_label(self):
        labels = copy.deepcopy(self.__destination)

        header_label = ['']
        header_label.extend(labels)
        header_label.extend(['Supply'])

        return header_label

    def __new_rows_label(self):
        labels = copy.deepcopy(self.__source)

        rows_label = ['']
        rows_label.extend(labels)
        rows_label.extend(['Demand'])

        return rows_label

    # -- Grid setter --
    def __set_widget_grid(self, header_label, rows_label):
        col_num = len(header_label)
        row_num = len(rows_label)

        self.__set_widget_label(header_label, rows_label)
        self.__set_widget_input(row_num, col_num)

    # -- Label setter --
    def __set_widget_label(self, header_label, rows_label):
        self.__set_header_label(header_label)
        self.__set_rows_label(rows_label)

    def __set_header_label(self, header_label):
        n = len(header_label)

        for i in range(0, n):
            Label(self.__widget, text=header_label[i]).grid(row=0, column=i)

    def __set_rows_label(self, rows_label):
        n = len(rows_label)

        for i in range(0, n):
            Label(self.__widget, text=rows_label[i]).grid(row=i, column=0)

    # -- Input setter --
    def __set_widget_input(self, row_num, col_num):
        rows = []

        for i in range(1, row_num):
            cols = []

            for j in range(1, col_num):
                if i.__eq__(row_num - 1) and j.__eq__(col_num - 1):
                    continue

                e = Entry(self.__widget)
                e.grid(row=i, column=j, sticky=SE)
                e.insert(END, 0)
                cols.append(e)

            rows.append(cols)

        self.__set_rows(rows)

    # -- Action method --
    def on_ok_button_pressed(self):
        rows = copy.copy(self.__rows)
        int_rows = self.__row_to_int(rows)

        self.__set_rows(int_rows)
        self.__widget.destroy()

    # -- Convert rows to int --
    @staticmethod
    def __row_to_int(rows):
        return [list(map(lambda x: int(x.get()), row)) for row in rows]

    # -- Setter methods for private access --
    def __set_rows(self, rows):
        self.__rows = rows

    # -- Getter methods for public access --
    def get_cost(self):
        rows = copy.copy(self.__rows)
        return [row[:-1] for row in rows[:-1]]

    def get_supply(self):
        rows = copy.copy(self.__rows)
        return [row[-1] for row in rows[:-1]]

    def get_demand(self):
        rows = copy.copy(self.__rows)
        return rows[-1]
