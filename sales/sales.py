# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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

    # your code
    while True:
        list_options = ["Show_table",
                        "Add",
                        "Remove",
                        "Update",
                        "Get_lowest_price_item_id",
                        "Get_items_sold_between"]
    
        ui.print_menu("Sales", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('sales/sales.csv')
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
                result = get_lowest_price_item_id(table)
                label = "Id of the item that was sold for the lowest price is: "
                ui.print_result(result, label)
            elif option == "6":
                input1 = ui.get_inputs(["month", "day", "year"],"Enter first date")
                month_from = input1[0]
                day_from = input1[1]
                year_from = input1[2]
                input2 = ui.get_inputs(["month", "day", "year"],"Enter second date")
                month_to = input2[0]
                day_to = input2[1]
                year_to = input2[2]
                
                result = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
                label = "Items sold between dates: "
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
    title_list = ['id_', 'title', 'price', 'month', 'day', 'year']
    
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
    user_input = ui.get_inputs(['title', 'price', 'month', 'day', 'year'],"Please provide your personal information")
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record] 
    data_manager.write_table_to_file('sales/sales.csv', table)
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
    data_manager.write_table_to_file('sales/sales.csv', table)
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
    user_input = ui.get_inputs(['title', 'price', 'month', 'day', 'year'],"Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2], item1[3], item1[4] = user_input[0], user_input[1], user_input[2], user_input[3]
    data_manager.write_table_to_file('sales/sales.csv', table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    # your code
    list_of_price = []
    list_of_tittle = []
    lenght_table = len(table)
    for i in range(lenght_table):
        list_of_price.append(table[i][2])
        minimal_value = int(min(list_of_price))
    for item in table:
        if int(item[2]) == minimal_value:
            list_of_tittle.append(item[1])
            best_title = min(list_of_tittle)
    for item in table:
        if item[1] == best_title:
            return(item[0])


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    # your code
    table_from_to = []

    for item in table:
        if int(item[5]) > year_from:
            table_from_to.append(item)
        elif int(item[5]) == year_from:
            if int(item[3]) > month_from:
                table_from_to.append(item)
            elif int(item[3]) == month_from:
                if int(item[4]) >= day_from:
                    table_from_to.append(item)

    for item in table_from_to:
        if int(item[5]) > year_to:
            table_from_to.remove(item)
        elif int(item[5]) == year_to:
            if int(item[3]) > month_to:
                table_from_to.remove(item)
            elif int(item[3]) == month_to:
                if int(item[4]) >= day_to:
                    table_from_to.remove(item)
    
    for list1 in table_from_to:
        for i in range(2,6): 
            list1[i] = int(list1[i])
    
    return table_from_to
