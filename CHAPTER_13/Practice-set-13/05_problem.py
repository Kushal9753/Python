''' Write a program to find the maximum of the numbers in a list using the reduce 
function. '''

from functools import reduce
a = [1,2,3,2,3,85,46,55,98,6]

def greater(a,b):
  if(a>b):
    return a
  return b

print(reduce(greater,a))