# HashCracker

## Description

HashCracker is a small project that consists of two python scripts: `hasher.py` and `cracker.py`. The `hasher.py` script takes a list of passwords and creates usernames in format `userXXX` (where `XXX` are three digits) and then hashes the passwords with SHA-256 hash function and finally writes the resulting username-password hash pairs to a file. The `cracker.py` script compares a list of password hashes to a list of popular password hashes and writes username-password pairs to a file if there is a match.

## Usage

1. Run `hasher.py`:

```
python hasher.py
```

2. Run `cracker.py`:

```
python cracker.py
```

## Requirements

* Python 3.x
* hashlib
* csv

## Inputs

* `hasher.py` takes a csv file `passwords.csv` as input.
* `cracker.py` takes two csv files as input: `user_password_hashes.csv` and `popular.csv`.

## Outputs

* `hasher.py` outputs a csv file `user_password_hashes.csv`.
* `cracker.py` outputs a txt file `hits.txt`.

## Note

The provided code is only intended to demonstrate the basic functionality of hashing and password cracking, it is not intended to be used for any malicious purposes or in a production environment. Use it at your own risk.
