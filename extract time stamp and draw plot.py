# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:09:23 2023
Extract timestamps and draw a plot from a pcap file

@author: AL-AMIN
"""

import matplotlib.pyplot as plt
import numpy as np
from scapy.all import rdpcap

# Set the window size and time interval for binning packets
window_size = 10  # seconds
time_interval = 1  # second

# Read the pcap file and extract packet data
packets = rdpcap('ddos_attack_packet_capture.pcap')

# Extract the timestamps from the packets
timestamps = [packet.time for packet in packets]

# Compute the number of bins needed
num_bins = int(np.ceil((timestamps[-1] - timestamps[0]) / time_interval))

# Initialize lists to store packet counts and bin start times
packet_counts = [0] * num_bins
bin_start_times = [timestamps[0] + i * time_interval for i in range(num_bins)]

# Bin the packets by time and count the number of packets in each bin
for timestamp in timestamps:
    bin_index = int(np.floor((timestamp - timestamps[0]) / time_interval))
    packet_counts[bin_index] += 1

# Compute the average packet count for each bin
avg_packet_counts = [count / window_size for count in packet_counts]

# Plot the average packet counts vs. bin start times
plt.plot(bin_start_times, avg_packet_counts)
plt.xlabel('Time (seconds)')
plt.ylabel('Average Packet Count')
plt.title(f'Average Packet Count per {window_size}-second Window')
plt.show()

