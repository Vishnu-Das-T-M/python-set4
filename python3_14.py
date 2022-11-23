#Write a Python program to combine each line from first file with the corresponding line in second file.

with open("x.txt") as xh:
  with open('y.txt') as yh:
    with open("z.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists  and Write to third file
      for line1, line2 in zip(ylines, xlines):
        zh.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))