#Write a Python program to read a random line from a file.

import random
lines = open('test.txt').read().splitlines()
myline =random.choice(lines)
print(myline)