import os

file_path = "record.tx"

def load_total_chars():
    with open(file_path, "r") as f:
        return int(f.read())

def set_total_chars(total_chars):
    with open(file_path, "w") as f:
        f.write(str(total_chars))