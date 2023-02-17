import csv
import hashlib
popular_hashes = []

hits = open("hits.txt", "w")

# takes a password as input, 
# converts it to a byte string encoded in utf-8,
# creates a SHA256 hash object, 
# and returns the hexadecimal representation of the hash digest.
def hash_pass(password):
    hash_obj = hashlib.sha256(password.encode())
    hex_dig = hash_obj.hexdigest()
    return hex_dig

with open("user_password_hashes.csv", "r") as csv_pass_hashes:
    # reads a list of usernames and their respective password hashes 
    pass_hashes = csv.reader(csv_pass_hashes, delimiter=" ")

    with open("popular.csv", "r") as csv_popular_passwords:
        # reads a file with popular passwords 
        popular_passwords = csv.reader(csv_popular_passwords, delimiter=" ")
        for row in popular_passwords:
            # hash every one of the popular passwords
            popular_hashes.append([row, hash_pass("".join(row))])
       
        for hash1 in pass_hashes:
            for popular_hash in popular_hashes:
                # compare user password hash with popular password hash
                if hash1[1] == popular_hash[1]:
                    # the hashes match, so write to hits-file the username
                    # along with the popuplar password
                    hits.write("{} {}\n".format(hash1[0], popular_hash[0]))
