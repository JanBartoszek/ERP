# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        list_options = ["show_table",
                        "add",
                        "remove",
                        "update",
                        "get_counts_by_manufacturers",
                        "get_average_by_manufacturer"]
        ui.print_menu("\nStore:\n", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('store/games.csv')
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(["id_"],"Enter record id")[0]
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(["id_"],"Enter record id")[0]
                update(table, id_)
            elif option == "5":
                result = get_counts_by_manufacturers(table)
                label = '\nManufacturers with number of their different titles in shop:\n'
                ui.print_result(result, label)
            elif option == "6":
                manufacturer = ui.get_inputs(["\nPlease enter manufacturer:\n"],"")[0]
                result = get_average_by_manufacturer(table, manufacturer)
                label = "Average number of games by {} in shop:".format(manufacturer)
                ui.print_result(result, label)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(err)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['id_', 'Title', 'manufacturer', 'price', 'in_stock']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    user_input = ui.get_inputs(['Title', 'manufacturer', 'price', 'in_stock'],"Please provide information")
    while common.is_number(user_input[2]) is False:
        ui.print_error_message('Error: Price value must be number')
        continue
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record] 
    data_manager.write_table_to_file('store/games.csv', table)
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
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                table.remove(item1)
    data_manager.write_table_to_file('store/games.csv', table)
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
    user_input = ui.get_inputs(['Title', 'manufacturer', 'price', 'in_stock'],"Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2], item1[3], item1[4] = user_input[0], user_input[1], user_input[2], user_input[3]
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturers_dict = {}
    for item in table:
        if item[2] not in manufacturers_dict:
            manufacturers_dict[item[2]] = 1
        else:
            manufacturers_dict[item[2]] += 1
    return manufacturers_dict


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    counter1 = 0
    counter2 = 0
    for item1 in table:
        for item2 in item1:
            if item2 == manufacturer:
                counter1 += 1
                counter2 += int(item1[4])
    result = counter2 / counter1
    return result
