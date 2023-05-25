#!/usr/local/bin/python3
import os

file_name = 'hex.txt'
ascii_file_name = 'hex_to_ascii.txt'
dir_path = '/Users/t.kimura/vagrant/vmkali/work/thm/c4ptur3-th3-fl4g/files'

file_path = os.path.join(dir_path, file_name)

def hex_to_string(bin_values):
    # int() convert hex to decimal
    # chr() convert decimal to charactor
    # .join() combine strings in a list

    # List Comprehensions -> Python Crash Course rev.2 pp.59-60
    # chr(int(i, 2)) is the value I want to store in the new list

    return ''.join([chr(int(i, 16)) for i in bin_values])

# read the file written in binary
with open(file_path, mode='r') as f:
    bin_values = f.read().split()
    # print(bin_values)
    s = hex_to_string(bin_values)
    print(s)

# write the file written in ascii
with open (ascii_file_name, 'w') as f:
    f.write(s)