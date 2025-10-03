class Employee:
  name = "Kushal"
  language = "py"
  salary = 1200000

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")
  
  @staticmethod
  def greet():
    print("good morning")



kushal = Employee() # object
kushal.language = "javascript"

kushal.greet()
kushal.getInfo()
# Employee.getInfo(kushal)