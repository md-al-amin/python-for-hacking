# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:28:02 2022

Making http request
Ref: Mastering Python for Networking and Security - Second Bdition  By José Manuel Ortega
@author: AL-AMIN
"""

import requests, json
print("Requests Library tests.")
response = requests.get("http://www.python.org")
print(response.json)


print("Status code: "+str(response.status_code))

print("***** Headers response:  ***** \n")

for header, value in response.headers.items():
    print(header, '-->', value)

print(" \n ***** Headers request :   ******  ")
for header, value in response.request.headers.items():
    print(header, '-->', value)
    
    
"""
import requests
if __name__ == "__main__":
 response = requests.get("http://www.python.org")
 for header in response.headers.keys():
     print(header + ":" + response.headers[header])
     
"""



