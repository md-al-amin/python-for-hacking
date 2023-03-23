# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:34:52 2023
Plot the result of several window size from a pcap file captured from ddos attack
@author: AL-AMIN
"""

import matplotlib.pyplot as plt
from scapy.all import rdpcap

# Set the window sizes to be plotted
window_sizes = [10, 50, 100, 500]

# Read the pcap file and extract packet data
packets = rdpcap('ddos_attack_packet_capture.pcap')

# Initialize lists to store data for each window size
packet_counts = []
timestamps = []

# Loop through each window size
for window_size in window_sizes:
    # Initialize variables for counting packets and tracking time
    count = 0
    start_time = packets[0].time
    end_time = start_time + window_size

    # Loop through each packet
    for packet in packets:
        # If the packet is within the current window, increment the count
        if packet.time >= start_time and packet.time < end_time:
            count += 1
        # If the packet is outside the current window, store the data and move to the next window
        else:
            packet_counts.append(count)
            timestamps.append(start_time)
            count = 1
            start_time = end_time
            end_time += window_size

    # Store the data for the last window
    packet_counts.append(count)
    timestamps.append(start_time)

    # Plot the data for the current window size
    plt.plot(timestamps, packet_counts, label=f'Window Size: {window_size}')

    # Reset the lists for the next window size
    packet_counts = []
    timestamps = []

# Add labels and legend to the plot
plt.xlabel('Time (seconds)')
plt.ylabel('Packet Count')
plt.title('Packet Count vs Time for Different Window Sizes')
plt.legend()

# Show the plot
plt.show()
