#!/usr/bin/env python3
# Remember that python is a dynamically typed language
# Mutable = can edit variable after creation
# Immutable = cannot edit variable after creation

# The following are composite data types in python
#   List = mutable
#   Tuple = immutable
#   Dictionary = mutable
#   Frozen Set = immutable
#   Set = mutable

# list can contain different data types and it is ordered and changeable
our_list = ["apple", "banana", "cherry", 1.5, 2, 3]
print(our_list) # prints ['apple', 'banana', 'cherry', 1.5, 2, 3]

# set is a collection of unordered and unindexed elements and it is mutable
our_set = {"apple", "banana", "cherry", 1.5, 2, 3}
print(our_set) # prints {1.5, 2, 3, 'apple', 'banana', 'cherry'}

# tuple is a collection of ordered and unchangeable elements
our_tuple = ("apple", "banana", "cherry", 1.5, 2, 3)
print(our_tuple) # prints ('apple', 'banana', 'cherry', 1.5, 2, 3)

# dictionary is a collection of key value pairs and it is unordered and changeable
our_dictionary = {"apple": 1, "banana": 2, "cherry": 3, "d":"somthing"}
print(our_dictionary) # prints {'apple': 1, 'banana': 2, 'cherry': 3, 'd': 'somthing'}

# frozen set is a collection of unordered and unindexed elements and it is immutable
our_frozen_set = frozenset({"apple", "banana", "cherry", 1.5, 2, 3})
second_frozen_set = frozenset(our_set)
print(our_frozen_set) # prints frozenset({1.5, 2, 3, 'apple', 'banana', 'cherry'})
print(second_frozen_set) # prints frozenset({1.5, 2, 3, 'apple', 'banana', 'cherry'})

