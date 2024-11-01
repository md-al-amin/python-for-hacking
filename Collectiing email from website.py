#Python program for collecting email

import csv
import re
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# Define regex pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Read input file containing URLs
with open('website.txt', 'r') as input_file:
    start_urls = input_file.read().splitlines()

# Initialize a set to store unique email addresses
unique_emails = set()

# Initialize a set to store visited URLs
visited_urls = set()

# Define a function to crawl a website
def crawl_website(url):
    # Send GET request to URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Search HTML content for email addresses
    email_matches = re.findall(email_pattern, soup.get_text())
    
    # Add unique email addresses to the set
    for email in email_matches:
        unique_emails.add(email)
    
    # Extract the domain name and sub domain from the URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    sub_domain = parsed_url.hostname.split('.')[0]
    website = f"{sub_domain}.{domain}"
    
    # Add the URL to the set of visited URLs
    visited_urls.add(url)
    
    # Find internal links on the page and recursively crawl them
    for link in soup.find_all('a', href=True):
        href = link['href']
        if not href.startswith('http'):
            href = urljoin(url, href)
        if href.startswith(url) and href not in visited_urls:
            crawl_website(href)
    
    print(f"Crawled {url}")

# Crawl each website in the input file
for start_url in start_urls:
    crawl_website(start_url)

# Open output file for writing unique email addresses in CSV format
with open('emails.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Website', 'Email'])

    for email in unique_emails:
        # Extract the domain name and sub domain from the email address
        parsed_email = urlparse(f"//{email}")
        domain = parsed_email.netloc
        sub_domain = parsed_email.hostname.split('.')[0]
        website = f"{sub_domain}.{domain}"
        writer.writerow([website, email])
