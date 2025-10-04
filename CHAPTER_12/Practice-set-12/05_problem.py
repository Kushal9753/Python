'''Store the multiplication tables generated in problem 3 in a file named Tables.txt.'''

n = int(input("enter the no. "))

table = [n*i for i in range(1, 11) ]

with open("tables.txt", "a") as f:
  f.write(f"table of {n}: {str(table)}\n")