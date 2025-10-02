# Write a program to calculate the factorial of a given number using for loop. 

n = int (input("Enter the number: "))

i = 1
fact = 1
for i in range(1, n+1):
  fact = fact*i
  i+=1

print(f"The factorial of {n} is {fact}")