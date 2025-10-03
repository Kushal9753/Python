# Write a recursive function to calculate the sum of first n natural numbers. 

def sum(n):
  if(n==0):
    return 0
  return n + sum(n-1)

a = int(input("Enter the number "))

b = sum(a)
print(f"Sum of {a} natural number is {b}")