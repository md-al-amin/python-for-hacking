# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:32:50 2023

@author: Alamin


"""

import hashlib

# Function to generate different types of hashes
def generate_hashes(input_str):
    # SHA1 hash
    sha1_hash = hashlib.sha1(input_str.encode('utf-8')).hexdigest()
    print(f"SHA1 hash: {sha1_hash}")

    # SHA256 hash
    sha256_hash = hashlib.sha256(input_str.encode('utf-8')).hexdigest()
    print(f"SHA256 hash: {sha256_hash}")

    # SHA512 hash
    sha512_hash = hashlib.sha512(input_str.encode('utf-8')).hexdigest()
    print(f"SHA512 hash: {sha512_hash}")

    # MD5 hash
    md5_hash = hashlib.md5(input_str.encode('utf-8')).hexdigest()
    print(f"MD5 hash: {md5_hash}")

    # NTLM hash
    ntlm_hash = hashlib.new('md4', input_str.encode('utf-16le')).hexdigest()
    print(f"NTLM hash: {ntlm_hash}")

    # LANMAN hash
    input_str = input_str.upper().encode('utf-8')
    if len(input_str) < 14:
        input_str += b'\x00' * (14 - len(input_str))
    lmhash = hashlib.new('md4', input_str[:14]).hexdigest()
    print(f"LANMAN hash: {lmhash}")

# Ask the user for input
input_str = input("Enter a string to hash: ")

# Generate hashes for the input string
generate_hashes(input_str)
