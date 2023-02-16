import socket
import pyfiglet
import sys
from datetime import datetime
import re




ascii_baner = pyfiglet.figlet_format("The best Port Scanner of All Time!")
print(ascii_baner)

target = input("Target IP: ")
if 6 > len(target) or len(target)> 15:
    print("This is not a valid IP address!")

print("_" * 50)
print("Scanning target: ", target)
print("Scan started on: ", str(datetime.now()))
print("_" * 50)
count = 0
try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.0001)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Found Open Port", {port})
            count += 1
        if port == 65535:
            print(f"Scan Completed! Found {count} opened ports!")
        s.close()
except(KeyboardInterrupt):
    print("\n Bye bye :(")
    sys.exit()
except(socket.error):
    print("\ Host not responding :(")
    sys.exit()
