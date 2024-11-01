# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:19:58 2023
Password generation using characters, digits and punctuations
"""

import itertools
import string

length = int(input("Enter the length of the strings: "))
filename = input("Enter the filename to save the strings: ")

# define the character set
characters = string.ascii_letters + string.digits + string.punctuation

# generate all possible combinations of the characters
combinations = itertools.product(characters, repeat=length)

# write the combinations to the file
with open(filename, 'w') as f:
    for combination in combinations:
        string = ''.join(combination)
        f.write(string + '\n')

