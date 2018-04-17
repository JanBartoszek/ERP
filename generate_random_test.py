import random


def hshhfdgf(table):
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
        print(generated)
        return generated


table = [['m^r1^SM6', 'gy6E}|E9'], ['qV*!qL58', 'Q%b+7Sv8']]


hshhfdgf(table)