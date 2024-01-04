#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10

response_format = "Last digit of {} is {} {}"

if last_digit == 0:
    print(response_format.format(number, last_digit, "zero"))
elif last_digit > 5:
    print(response_format.format(number, last_digit, "and is greater than 5"))
else:
    print(response_format.format(number, last_digit, "and is less than 6 and not 0"))

