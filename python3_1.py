#Write a Python program to read an entire text file.

try:
    f = open("test.txt", "r")
    print(f.read())
finally:
    f.close()    