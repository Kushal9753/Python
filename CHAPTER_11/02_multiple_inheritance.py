class Employee:
  name = "Default name"
  company1 = "ITC"
  def show(self):
    print(f"The name is {self.name} and the salary is {self.company1}")

class Coder():
  language = "python"
  def printLanguages(self):
    print(f" out of all languages here is your language: {self.language}")

class Programmer(Employee, Coder):
  company = "ITC Infotech"
  def showLanguage(self):
      print(f"The name is {self.company} and the salary is {self.name}")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()