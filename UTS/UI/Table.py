from terminaltables import AsciiTable
from dashtable import data2rst


def show_init_table(source, destination, cost, demand, supply):
    header = ['']
    header += destination
    header += ['Supply']

    rows = []
    for i in range(len(source)):
        row = [source[i]]
        rows.append(row)

    for i in range(len(cost)):
        for j in range(len(cost[0])):
            rows[i].append(cost[i][j])

    for i in range(len(source)):
        rows[i].append(supply[i])

    footer = ['Demand'] + demand

    table_data = []

    table_data.append(header)
    for row in rows:
        table_data.append(row)
    table_data.append(footer)

    table = AsciiTable(table_data)
    print(table.table)
    # print(data2rst(table_data, use_headers=False))

