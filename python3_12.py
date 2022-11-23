#Write a Python program to write a list to a file.

MyList = ["New York", "London", "Paris", "New Delhi"]
MyFile=open('output.txt','w')

for element in MyList:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()