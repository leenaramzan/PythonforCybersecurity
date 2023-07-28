# import modules
import os
import crypt

# fuction to test password
def test_password(algorithm_salt, hashed_password, password_guess):
    # use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    # compare salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

# load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top1000.txt", "r")
passwords = f.readlines()

# prompt user for algorithm/salt
algorithm_salt = input("What is the algorithm and salt? ")
# prompt user for salted hash
hashed_password = input("What is the full hashed password? ")
# loop through each password
for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("Match found: {0}".format(password))
        break
