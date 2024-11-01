# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:52:15 2023
Rainbow Table program 
@author: AL-AMIN
"""
#import random
import hashlib

# Define the character set
charset = 'abc123'

# Define the password length
password_length = int(input("Please Enter the length of password :  "))

# Generate all possible plaintext passwords
plaintexts = []
for i in range(len(charset)):
    for j in range(len(charset)):
        for k in range(len(charset)):
            for l in range(len(charset)):
                for m in range(len(charset)):
                    for n in range(len(charset)):
                        plaintext = charset[i] + charset[j] + charset[k] + charset[l] + charset[m] + charset[n]
                        plaintexts.append(plaintext)

# Create the rainbow table
rainbow_table = {}
for plaintext in plaintexts:
    hash_value = hashlib.md5(plaintext.encode()).hexdigest()
    reduced_value = hash_value[:password_length]
    if reduced_value not in rainbow_table:
        rainbow_table[reduced_value] = plaintext

# Save the rainbow table to a file
with open('rainbow_table.txt', 'w') as file:
    for key, value in rainbow_table.items():
        file.write(f"{key}:{value}\n")
