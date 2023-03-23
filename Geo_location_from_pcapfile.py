# -*- coding: utf-8 -*-
"""
Find out GEO Location of IP address from a .pacp file.
Created on Wed Mar 22 22:16:07 2023

@author: AL-AMIN
"""
import geoip2.database
import collections
from scapy.all import rdpcap

# Load GeoLite2 database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Read the pcap file and extract packet data
packets = rdpcap('ddos_attack_packet_capture.pcap')

# Initialize a counter for the number of packets from each country
country_counts = collections.Counter()

# Extract the source IP address from each packet and get its country
for packet in packets:
    if 'IP' in packet:
        src_ip = packet['IP'].src
        try:
            response = reader.country(src_ip)
            country = response.country.iso_code
            if country is not None:
                country_counts[country] += 1
        except geoip2.errors.AddressNotFoundError:
            pass

# Print a table of the top 10 countries of origin
print('Top 10 Countries of Origin:')
print('===========================')
for country, count in country_counts.most_common(20):
    print(f'{country}: {count}')
