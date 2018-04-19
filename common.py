# implement commonly used functions here

import random


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
