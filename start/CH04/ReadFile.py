#!/usr/bin/env python3
# Sample script that reads from a file
# By 

ip_file = open("hackme.txt", "r")
ip_addresses = ip_file.read()
print(ip_addresses)
ip_file.close()