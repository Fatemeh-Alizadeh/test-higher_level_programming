#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints x elements of list"""

    str_len = 0
    for i in my_list:
        str_len = str_len + 1

    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
        print("")
        return count
    except IndexError:
        raise
