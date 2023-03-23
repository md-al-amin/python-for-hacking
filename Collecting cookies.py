# -*- coding: utf-8 -*-
"""
Spyder Editor

Collecting cookies form a specific websites
MD AL AMIN.
"""

import requests

# Get website name from user input
website = input("Enter website URL: ")

# Send a GET request to the website
response = requests.get(website)

# Get the cookies from the response object
cookies = response.cookies

# Print the cookies
print(cookies)

