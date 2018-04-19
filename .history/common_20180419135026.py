# implement commonly used functions here

import random
import ui


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    # your code
    a = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')for _ in range(2))
    b = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(2))
    c = ''.join(random.choice('1234567890')for _ in range(2))
    d = ''.join(random.choice('!@#$%^&*()+-=}{|[]\:"<>?/.,')for _ in range(2))
    e = ''.join(a + b + c + d)
    generated = ''.join(random.sample(e, len(e)))

    contain = False
    for list1 in table:
        for list2 in list1:
            if list2 == generated:
                contain = True

    if contain is False:
        return generated


def check_length(user_inp):
    for item in user_inp:
        if len(item) > 30:
            ui.print_error_message("\nInput too long!\n")
            return False


# def check_user_inp(labels, check_function):
def check_user_inp(labels,i):
        user_inp = []
        for item in labels:
            acceptable_inp = False
            while acceptable_inp is False:
                user_single_inp = ui.get_inputs([item], "Please provide information")
                if check_length(user_single_inp) is not False:
                    if item == labels[i]:
                        print(item)
                        print(labels[i])
                        print(user_single_inp)
                        
                        if is_number(*user_single_inp) is True:
                            print('istru')
                            user_inp.append(*user_single_inp)
                            acceptable_inp = True
                        else: 
                            print('isnottru')
                            acceptable_inp = False
                    user_inp.append(*user_single_inp)
                    acceptable_inp = True
                # if item == in range(2, 4):

        return user_inp
def is_number(number_text):
    print(number_text)
    print(type(number_text))
    try:
        int(number_text)
        return True
    except Exception:
        return False
