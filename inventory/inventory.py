# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
# date time
import datetime
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# date time


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # you code
    while True:
        list_options = ["Show_table",
                        "Add",
                        "Remove",
                        "Update",
                        "Get_available_items",
                        "Get_average_durability_by_manufacturers"]

        ui.print_menu("Inventory", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('inventory/inventory.csv')
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(["id_"], "Enter record id")[0]
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(["id_"], "Enter record id")[0]
                update(table, id_)
            elif option == "5":
                label = 'Available items'
                table = get_available_items(table)
                ui.print_result('', label)
                if table == []:
                    ui.print_error_message('All items are overdue')
                else:
                    show_table(table)
            elif option == "6":
                label = 'Avarge durability'
                result = get_average_durability_by_manufacturers(table)
                ui.print_result(result, label)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(err)
    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ['id_', 'name', 'manufacturer', 'purchase_date', 'durability']

    ui.print_table(table, title_list)
    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code
    user_input = ui.get_inputs(['name', 'manufacturer', 'purchase_date', 'durability'], 
                               "Please provide your personal information")
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record]
    data_manager.write_table_to_file('inventory/inventory.csv', table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                table.remove(item1)
    data_manager.write_table_to_file('inventory/inventory.csv', table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code
    user_input = ui.get_inputs(['name', 'manufacturer', 'purchase_date', 'durability'], "Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2], item1[3], item1[4] = user_input[0], user_input[1], user_input[2], user_input[3]
    data_manager.write_table_to_file('inventory/inventory.csv', table)
    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists


def get_available_items(table):
    now = datetime.datetime.now()
    current_year = now.year - 1

    not_overdue = []
    for item in table:
        if (int(item[3])+int(item[4])) >= int(current_year):
            not_overdue.append(item)

    for item in not_overdue:
        for item2 in range(3, 5):
            item[item2] = int(item[item2])

    return not_overdue


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    manufactures = list(set([row[2] for row in table]))
    item_of_items = [[int(row[4]) for row in table if row[2] == item] for item in manufactures]
    avg_durability = []
    for listofavg in item_of_items:
        suma = 0
        count = 0
        for elem in listofavg:
            suma += elem
            count += 1
        avg_durability.append(suma/count)
    result = {manufactures[i]: avg_durability[i] for i in range(0, len(manufactures))}
    return result
