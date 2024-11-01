# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:42:22 2023
Collecting email address from a webpage
@author: AL-AMIN
"""

import csv
import re
import requests
from urllib.parse import urlparse

# Define regex pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Read input file containing URLs
with open('webpage.txt', 'r') as input_file:
    urls = input_file.read().splitlines()

# Initialize a dictionary to store website names and their corresponding email addresses
email_dict = {}

# Iterate over URLs
for url in urls:
    # Send GET request to URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        continue
        
    # Search response text for email addresses
    email_matches = re.findall(email_pattern, response.text)
    
    # Extract the domain name and sub domain from the URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    sub_domain = parsed_url.hostname.split('.')[0]
    website = f"{domain}"
    
    # Add unique email addresses to the dictionary
    for email in email_matches:
        if website not in email_dict:
            email_dict[website] = [email]
        else:
            if email not in email_dict[website]:
                email_dict[website].append(email)

# Open output file for writing unique email addresses in CSV format
with open('webpage_emails.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Website', 'Email'])

    for website, emails in email_dict.items():
        for email in emails:
            writer.writerow([website, email])
