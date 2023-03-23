# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:34:48 2023

@author: ChatGPT
"""


# Function to identify the type of hash
def identify_hash(hash_str):
    if len(hash_str) == 32:
        print("Hash type: MD5")
    elif len(hash_str) == 40:
        print("Hash type: SHA1")
    elif len(hash_str) == 64:
        print("Hash type: SHA256")
    elif len(hash_str) == 128:
        print("Hash type: SHA512")
    elif len(hash_str) == 32 or len(hash_str) == 33:
        print("Hash type: NTLM")
    else:
        print("Hash type not recognized")

# Ask the user for input
hash_str = input("Enter a hash to identify: ")

# Identify the type of hash
identify_hash(hash_str)
