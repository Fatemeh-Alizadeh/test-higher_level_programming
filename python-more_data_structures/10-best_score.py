#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    for k in a_dictionary:
        print(k)
        print(a_dictionary[k])
        if best is None or a_dictionary[k] > a_dictionary[best]:
            best = k
    return best
