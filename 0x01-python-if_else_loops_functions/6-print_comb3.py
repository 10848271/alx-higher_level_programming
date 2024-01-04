#!/usr/bin/python3
for num in range(0, 9):
    for num2 in range(num + 1, 10):
        if num < 8:
            print("{0:d}{1:d}".format(num, num2), end=", ")
        else:
            print("{0:d}{1:d}".format(num, num2))
