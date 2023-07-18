#!/usr/bin/env python3
# Sample script that writes to a file
# By Leena on 7/18

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Open file for writing
f = open(dir_path + "/hackme.txt", "w")

# Write to the file
print("What is your name?")
f.write("My name is Emily\n")
print("What is your favorite color?")
f.write("My favorite color is red\n")
print("What was your first pet's name?")
f.write("My first pet's name was Gabriel\n")
print("What is your mother's maiden name?")
f.write("My mother's maiden name is Dave\n")
print("What elementary school did you attend?")
f.write("I attended Mark Twain Elementary School\n")

# Close file
f.close()