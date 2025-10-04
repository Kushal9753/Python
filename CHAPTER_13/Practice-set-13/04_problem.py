''' Write a program to filter a list of numbers which are divisible by 5. '''

def divisible5(n):
  if(n%5 == 0):
    return True
  return False

a = [1,2,3,5456,3365,85,46,55,655,6]

f = list(filter(divisible5, a))

print(f)