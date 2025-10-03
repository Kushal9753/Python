# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
  compony = "Microsoft"
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin


p = Programmer("kushal", 1200000, 24244)
print(p.name, p.salary, p.pin)

r = Programmer("rohan", 100000, 2444)
print(r.name, r.salary, r.pin)