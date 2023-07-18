#!/usr/bin/env python3
# Sample script that reads from a file
# By Leena on 7/18

import os
dir_path + os.path.dirname(os.path.realpath(__file__))

# Open file for reading
f = open(dir_path + "/hackme.txt", "r")

# Read the file and print to screen
contents = f.read()
print(contents)

# Close the file
f.close()