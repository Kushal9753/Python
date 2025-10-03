f = open("file.txt")

# lines = f.readlines()

# line1 = f.readline()

# print(line1, type(line1))


# line2 = f.readline()

# print(line2, type(line2))



# line3 = f.readline()

# print(line3, type(line3))


line = f.readline()
while(line != ""):
  print(line)
  line = f.readline()


f.close()