#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
if(number < 0):
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    str1 = "and is greater than 5"
elif last_digit == 0:
    str1 = "and is 0"
elif last_digit < 6 and last_digit != 0:
    str1 = "and is less than 6 and not 0"

print(f"{str} {number} is {last_digit} {str1}")
