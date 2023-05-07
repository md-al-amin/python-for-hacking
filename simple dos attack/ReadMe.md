
# Simple Dos Attack Python Script

A Simple python code for Dos Attack

This is a simple Python program that sends multiple HTTP GET requests to a target URL using multiple threads. The main components of the code are explained below:

1. Importing libraries:
   - `import requests`: Imports the `requests` library, which is used to make HTTP requests.
   - `import threading`: Imports the `threading` library, which allows the creation and management of multiple threads.

2. User input:
   - `TARGET_URL`: Takes the target URL as input from the user.
   - `NUM_REQUESTS`: Takes the total number of requests to be sent as input from the user.
   - `NUM_THREADS`: Takes the number of threads to be used for sending requests as input from the user.

3. Defining the `send_requests` function:
   - This function sends HTTP GET requests to the target URL.
   - It loops for `NUM_REQUESTS // NUM_THREADS` times, ensuring that the total number of requests sent by all threads combined is equal to `NUM_REQUESTS`.
   - It uses the `requests.get()` function to send an HTTP GET request to the target URL.
   - It catches any `requests.exceptions.RequestException` that might occur during the request and ignores the error using the `pass` statement.

4. Main program execution:
   - The `if __name__ == "__main__":` line checks if the script is being run as the main program (as opposed to being imported as a module).
   - If the script is the main program, it creates an empty list called `threads`.
   - It then creates and starts `NUM_THREADS` threads, each running the `send_requests` function, and appends them to the `threads` list.
   - The `t.join()` loop waits for all threads to finish before proceeding.
   - Finally, it prints the total number of requests sent to the target URL.

