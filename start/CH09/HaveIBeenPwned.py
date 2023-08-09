#!/usr/bin/env python3
# Script that checks passwords against haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Leena

# import modules
import hashlib
import requests

# function to check passwords
def check_haveibeenphoned(sha_prefix):
    pwnd_dict = {}
    # Perform API request
    request_uri = "https://api.pnwedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)
    # Confirm if found
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwnd_dict[temp_pass[0]] = temp_pass[1]
    return pwnd_dict

# Ask for password
new_password = input("What password needs to be checked? ")

# Hash the password
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()
print(hashed_password)

# Split hash
sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5:].upper()

# Check the password hash
check_haveibeenphoned(sha_prefix)

# Check results
if sha_postfix in pwnd_dict.keys():
    print("Password has been compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
    print("Password has not been found, it is safe to use!")