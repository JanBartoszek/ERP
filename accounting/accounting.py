# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    # you code
    while True:
        list_options = ["Show_table",
                        "Add",
                        "Remove",
                        "Update",
                        "Which_year_max",
                        "Avg_amount"]

        ui.print_menu("Accounting manager", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('accounting/items.csv')
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
                result = which_year_max(table)
                label = "Highest profit year"
                ui.print_result(result, label)
            elif option == "6":
                year = ui.get_inputs(["Enter year"], "")[0]
                result = avg_amount(table, year)
                label = "Average profit per item in given year"
                ui.print_result(result, label)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(err)
    pass


def show_table(table):
    """#table=[[1,'1234','123','12',1],['12',123421423534535645756,'1','1',245],['12','1234',1,'1',345654754],['12','1234','1',11234,1]]
#title_list=['title1','title2','title3','title4',title5]
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ['id_', 'month', 'day', 'year', 'type', 'amount']

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
    user_input = ui.get_inputs(['month', 'day', 'year', 'type', 'amount'], "Please provide your personal information")
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record]
    data_manager.write_table_to_file('accounting/items.csv', table)
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
    data_manager.write_table_to_file('accounting/items.csv', table)
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
    user_input = ui.get_inputs(['month', 'day', 'year', 'type', 'amount'], "Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2], item1[3], item1[4] = user_input[0], user_input[1], user_input[2], user_input[3]
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)

def which_year_max(table):
    profit_per_year = []
    newest_year = 0
    for position in table:
        if int(position[3]) > int(newest_year):
            newest_year = position[3]
    else:
        pass
    years = []
    for position in table:
        if not position[3] in years:
            years.append(position[3])
            profit_per_year.append(0)
        else:
            pass
        if position[4] == 'out':
            profit_per_year[-int(position[3])+int(newest_year)] -= int(position[5])
        elif position[4] == 'in':
            profit_per_year[-int(position[3])+int(newest_year)] += int(position[5])
        else:
            ui.print_error_message('Error in data file')
    highest_profit = 0
    for profit in profit_per_year:
        if profit > highest_profit:
            highest_profit = profit
        else:
            pass
    i = 0
    for profit in profit_per_year:
        if profit == highest_profit:
            result = years[i]
            return int(result)
        else:
            i += 1


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code
    money = 0
    items_counter = 0
    for item in table:
        if int(item[3]) == int(year):
            items_counter += 1
            if item[4] == 'in':
                money += int(item[5])
            else:
                money -= int(item[5])
    return money/items_counter
