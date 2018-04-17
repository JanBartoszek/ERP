# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
                        "Get_oldest_person",
                        "Get_persons_closest_to_average"]
    
        ui.print_menu("Human resources manager", list_options, "Back to main")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            table = data_manager.get_table_from_file('hr/persons.csv')
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
                label='Oldest person'
                result=get_oldest_person(table)
                ui.print_result(result, label)
            elif option == "6":
                label='Person closest to avarge'
                result=get_persons_closest_to_average(table)
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
    title_list = ['id_', 'name', 'birth_date']
    
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
    user_input = ui.get_inputs(['name', 'birth_date'],"Please provide your personal information")
    new_id = common.generate_random(table)
    new_record = [new_id] + user_input
    table += [new_record] 
    data_manager.write_table_to_file('hr/persons.csv', table)
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
    data_manager.write_table_to_file('hr/persons.csv', table)
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
    user_input = ui.get_inputs(['name', 'birth_date'],"Please provide information")
    for item1 in table:
        for item2 in item1:
            if item2 == id_:
                item1[1], item1[2] = user_input[0], user_input[1]
    data_manager.write_table_to_file('hr/persons.csv', table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    result = []
    current_oldest = 9999
    for person in table:
        if int(person[2]) < int(current_oldest):
            current_oldest = person[2]
    for person in table:
        if int(person[2]) == int(current_oldest):
            result.append(person[1])
    return result
        
    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code
    result = []
    sum = 0
    smallest_diff = 200
    for person in table:
        sum += int(person[2])
    average = sum/len(table)
    for person in table:
        diff = average-int(person[2])
        if diff < 0:
            diff =- diff
        else:
            pass
        if diff < smallest_diff:
            smallest_diff = diff
        else:
            pass
    for person in table:
        diff = average-int(person[2])
        if diff == smallest_diff:
            result.append(person[1])
    return result
    pass
