# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:23:25 2023

@author: AL-AMIN
"""

import requests
import threading

TARGET_URL = input("Enter the target URL: ")
NUM_REQUESTS = int(input("Enter the number of requests: "))
NUM_THREADS = int(input("Enter the number of threads: "))

def send_requests():
    for _ in range(NUM_REQUESTS // NUM_THREADS):
        try:
            requests.get(TARGET_URL)
        except requests.exceptions.RequestException:
            pass

if __name__ == "__main__":
    threads = []

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=send_requests)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Sent {NUM_REQUESTS} requests to {TARGET_URL}")

