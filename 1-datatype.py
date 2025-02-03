#!/usr/bin/env python3

intage = 25
print(type(intage)) # prints <class 'int'>

floatage = 25.0
print(type(floatage)) # prints <class 'float'>

stringage = "25"
print(type(stringage)) # prints <class 'str'>

# Casting is the process of converting one data type to another
# we can do this with the int(), float(), and str() functions
casting = int(stringage) # converts string to integer
print(type(casting)) # prints <class 'int'>

# multi word variable names
days_in_a_week = "seven"
number_and_age = (floatage, days_in_a_week)
print(number_and_age) # prints (25.0, 'seven')