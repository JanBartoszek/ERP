# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
                        "Get_longest_name_id",
                        "Get_subscribed_emails"]
    
        ui.print_menu("Customers", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('crm/customers.csv')
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
                result = get_longest_name_id(table)
                label = '\nId of the customer with the longest name'
                ui.print_result(result, label)
            elif option == "6":
                result = get_subscribed_emails(table)
                label = '\nList of subscribers'
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
    title_list = ['id_', 'name', 'email', 'subscribed']
    
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
    user_input = ui.get_inputs(['name', 'email', 'subscribed'],"Please provide your personal information")
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record] 
    data_manager.write_table_to_file('crm/customers.csv', table)
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
    data_manager.write_table_to_file('crm/customers.csv', table)
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
    user_input = ui.get_inputs(['name', 'email', 'subscribed'],"Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2], item1[3] = user_input[0], user_input[1], user_input[2]
    data_manager.write_table_to_file('crm/customers.csv', table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code
    longest_name_entries = [['id', 'a']]
    for item in table:
        if len(item[1]) > len(longest_name_entries[0][1]):
            longest_name_entries = []
            longest_name_entries.append(item)
        elif len(item[1]) == len(longest_name_entries[0][1]):
            longest_name_entries.append(item)
    
    longest_names = []
    for item in longest_name_entries:
        longest_names.append(item[1])
    
    longest_name = min(longest_names)
    
    for item in longest_name_entries:
        if item[1] == longest_name:
            result = item[0]
    
    return result


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code
    list_of_subscribers = []
    for item in table:
        if item[3] == '1':
            list_of_subscribers.append('{}{}{}'.format(item[2], ';', item[1]))
    return list_of_subscribers
