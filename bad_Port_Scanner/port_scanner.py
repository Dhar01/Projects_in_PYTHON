#!/bin/python3

""" A simple & bad Port Scanner.
This script was made along with TCM Course.
How to scan: $ python3 port_scanner.py <your desired IP address>"""

import sys
import socket
from datetime import datetime

# defining target
if len(sys.argv) == 2:
    # translating hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

# adding banner to make it somewhat pretty.
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("Press ctrl-c to stop scanning.")
print("-" * 50)

try:
    for port in range(50, 85):
        # you can change the port range from 1 to (I forgot the number), anyway
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        # to check which port are scanning, uncomment the below
        # print("Checking port {}".format(port))

        if result == 0:
            print("Port {} is open".format(port))
            s.close()

# for error handling
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
