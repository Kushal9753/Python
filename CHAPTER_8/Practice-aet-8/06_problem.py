# Write a python function which converts inches to cms. 

def inch_to_cms(inch):
  return inch * 2.54

n = int(input("Enter the values in inches: "))

print(f"The values in cms is {inch_to_cms(n)}")