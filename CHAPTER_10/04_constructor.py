class Employee:
  name = "Kushal"
  language = "py"
  salary = 1200000

  def __init__(self, name, salary, language):     # dunder method which is automatically called
    self.name = name
    self.salary = salary
    self.language = language
    print("I am creating an object")

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")
  
  @staticmethod
  def greet():
    print("good morning")



kushal = Employee("Kushal", 13000000, "javascript") # object

print(kushal.name, kushal.language, kushal.salary)