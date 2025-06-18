#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        lenght = len(sentence)
        first_char = sentence[0]
        return (lenght, first_char)
