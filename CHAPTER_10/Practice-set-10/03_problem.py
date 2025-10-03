# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

# Ans = No

class Demo:
  a = 4


o = Demo()
print(o.Demo)

o.a = 0
print(o.Demo)