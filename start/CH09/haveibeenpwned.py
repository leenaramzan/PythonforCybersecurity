#!/usr/bin/env python3
# Script that checks passwords against haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Leena

# import modules
import hashlib
import requests

# function to check password
def check_haveibeenphoned(sha_prefix):
    pwnd_dict = {}
    # perform API request
    request_uri = "https://api.pwnedpasswords.com/range/" + sha_prefix
    results = requests.get(request_uri)
    # confirm if found
    pwned_list = results.text.split("\r\n")
    for pwnd_pass in pwned_list:
        temp_pass = pwnd_pass.split(":")
        pwnd_dict[temp_pass[0]] = temp_pass[1]
    return pwnd_dict


# ask for password 
new_password = input("What password need to be checked? ")

# Hash the password
encoded_password = new_password.encode()
digest_password = hashlib.sha1(encoded_password)
hashed_password = digest_password.hexdigest()

# Split hash
sha_prefix = hashed_password[0:5]
sha_postfix = hashed_password[5:]

# Check password hash
pwnd_dict = check_haveibeenphoned(sha_prefix)

# Check results
if sha_postfix in pwnd_dict.keys():
    print("Password has been compromised {0} times".format(pwnd_dict[sha_postfix]))
else:
    print("Password has not been found, it is safe to use!")
