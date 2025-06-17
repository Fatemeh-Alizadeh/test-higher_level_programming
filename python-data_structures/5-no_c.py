#!/usr/bin/python3

def no_c(my_string):
    return ''.join(char for char in my_string if char != 'c' and char != 'C')

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))