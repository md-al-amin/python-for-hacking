# -*- coding: utf-8 -*-
"""
Spyder Editor

Python code for port scanning.
Mr. Al-Amin.
"""

import socket

def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        print(f'Port {port} is open')
        return True
    except:
        print(f'Port {port} is closed')
        return False
    finally:
        s.close()

host = input("Please enthe the domain name: ")

for port in range(79, 83): #set a range for scanning
    port_scan(host, port)
