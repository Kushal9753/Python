# Write a program using functions to find greatest of three numbers. a

a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))

def greatest(a, b, c,):
  if(a>b and a>c):
    return a
  elif(b>a and b>c):
    return b
  elif(c>a and c>b):
    return c

g = greatest(a, b, c)

print(f"greatest is {g}")