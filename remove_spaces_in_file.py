#!/usr/local/bin/python3
import os

file_name = 'binary_with_spaces.txt'
new_file_name = 'binary.txt'
dir_path = '/Users/t.kimura/vagrant/vmkali/work/thm/c4ptur3-th3-fl4g/files'

file_path = os.path.join(dir_path, file_name)

# read the file written in binary and remove spaces
with open(file_path, mode='r') as f:
    txt = f.read().replace(' ', '')


# write the file written in binary without spaces
with open (new_file_name, 'w') as f:
    f.write(txt)



