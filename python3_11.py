#Write a Python program to get the file size of a plain file

import os
file_stat = os.stat('test.txt')
print(file_stat.st_size)