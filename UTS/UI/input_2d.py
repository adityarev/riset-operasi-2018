from tkinter import *

widget = Tk()
suppliers = ['Los Angeles', 'Detroit', 'New Orleans', 'Dummy Plant']
receivers = ['Denver', 'Miami']
rows = []


def main():
    header_label = get_header_label(receivers)
    rows_label = get_rows_label(suppliers)

    set_grid(header_label, rows_label)

    Button(text='Fetch', command=button_fetch_on_press)\
        .grid(row=len(rows_label), column=len(header_label)-1, sticky=SE, pady=4, padx=41)
    Button(widget, text='Quit', command=widget.quit)\
        .grid(row=len(rows_label), column=len(header_label)-1, sticky=SE, pady=4, padx=4)
    mainloop()


def get_header_label(labels):
    header_label = ['']
    header_label.extend(labels)
    header_label.extend(['Supply'])

    return header_label


def get_rows_label(labels):
    rows_label = ['']
    rows_label.extend(labels)
    rows_label.extend(['Demand'])

    return rows_label


def set_grid(header_label, rows_label):
    cols_num = len(header_label)
    rows_num = len(rows_label)

    set_widget_input(rows_num, cols_num)
    set_widget_label(header_label, rows_label)


def set_widget_input(rows_num, cols_num):
    for i in range(1, rows_num):
        cols = []

        for j in range(1, cols_num):
            if i == rows_num - 1 and j == cols_num - 1:
                continue

            e = Entry(widget)
            e.grid(row=i, column=j, sticky=SE)
            e.insert(END, 0.0)
            cols.append(e)

        rows.append(cols)


def set_widget_label(header_label, rows_label):
    set_header_label(header_label)
    set_rows_label(rows_label)


def set_header_label(header_label):
    n = len(header_label)

    for i in range(0, n):
        Label(widget, text=header_label[i]).grid(row=0, column=i)


def set_rows_label(rows_label):
    n = len(rows_label)

    for i in range(0, n):
        Label(widget, text=rows_label[i]).grid(row=i, column=0, sticky=NW)


def button_fetch_on_press():
    for row in rows:
        cols = []

        for col in row:
            cols.append(float(col.get()))

        print(cols)

if __name__ == '__main__':
    main()
