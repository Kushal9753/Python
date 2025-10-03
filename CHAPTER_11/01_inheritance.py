class Employee:
  company1 = "ITC"
  def show(self):
    print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
  # company = "ITC Infotech"
#   def show(self):
#      print(f"The name is {self.name} and the salary is {self.salary}")

#   def showLanguage(self):
#      print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
  company = "ITC Infotech"
  def showLanguage(self):
      print(f"The name is {self.name} and the salary is {self.salary}")


a = Employee()
b = Programmer()

print(b.company1, b.company)