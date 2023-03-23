# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 00:09:49 2023

@author: AL-AMIN
"""

import argparse
import hashlib

# Parse command line arguments
parser = argparse.ArgumentParser(description='Decrypt hash value from a wordlist')
parser.add_argument('hashfile', type=str, help='Name of the file containing the hash value to decrypt')
parser.add_argument('wordlist', type=str, help='Name of the file containing the wordlist of passwords')
args = parser.parse_args()

# Target hash value to decrypt
with open(args.hashfile, "r") as f:
    target_hash = f.read().strip()

# Wordlist of passwords to try
with open(args.wordlist, "r") as f:
    wordlist = f.read().splitlines()

# Try each password in the wordlist
for password in wordlist:
    # Compute hash value for the password using different hashing algorithms
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()

    # Compare the computed hash values with the target hash value
    if md5_hash == target_hash:
        print(f"MD5 hash matched: {password}")
    if sha1_hash == target_hash:
        print(f"SHA1 hash matched: {password}")
    if sha256_hash == target_hash:
        print(f"SHA256 hash matched: {password}")
    if sha512_hash == target_hash:
        print(f"SHA512 hash matched: {password}")


# run this program using command line python hash_decrypt.py <hashfile> <wordlist>