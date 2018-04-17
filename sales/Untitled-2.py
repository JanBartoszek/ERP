import os
# User interface module
# data manager module
import data_manager
# common module
import common


table = get_table_from_file('sales.csv')

row_format ="{:>15}" * (len(table) + 1)
print(row_format.format("", *table))
for team, row in zip(table, data):
    print(row_format.format(team, *row))