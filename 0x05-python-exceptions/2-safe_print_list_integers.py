#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_count = 0
    if x <= 0:
        return print_count
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            print_count += 1
        except  (TypeError, ValueError):
            pass
    print()
    return print_count
