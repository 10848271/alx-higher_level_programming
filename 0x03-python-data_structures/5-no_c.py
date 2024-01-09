#!/usr/bin/python3

def no_c(my_string):
    no_c = ""
    for c in my_string:
        if ord(c) == ord('c') or ord(c) == ord('C'):
            continue
        no_c += c
    return no_c
