class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printFirstName(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
billSmith = Person("Bill",29)
p1.printFirstName()
billSmith.printFirstName()
