import csv
import hashlib

user_index = 1
hash_dict = {}

# takes a password as input, 
# converts it to a byte string encoded in utf-8,
# creates a SHA256 hash object, 
# and returns the hexadecimal representation of the hash digest.

def hash_pass(password):
    hash_obj = hashlib.sha256(password.encode())
    hex_dig = hash_obj.hexdigest()
    return hex_dig

# opens a file with user passwords and
# creates a username with format userXXX (0-999) for every password
# finally hashes the password and stores every user and their password to a dictionary  
with open("passwords.csv") as csv_pass:
    csv_pass = csv.reader(csv_pass, delimiter=" ")
    for row in csv_pass:
        # create username userXXX
        username = "user" + "{:03}".format(user_index)
        user_index += 1
        # add username along with hashpassword to dictionary
        hash_dict[username] = hash_pass("".join(row))

# write the dictionary of usernames and their password hashes to an output file
with open("user_password_hashes.csv", "w") as output_file:
    for uname, pass_hash in hash_dict.items():
        output_file.write("{} {}\n".format(uname, pass_hash))
