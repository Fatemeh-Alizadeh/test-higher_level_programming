#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except Exception as e :
        print(e)
        result = None
    finally:
        print("{}".format(result))
    return result
