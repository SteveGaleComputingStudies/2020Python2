class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):
    return(self.name)

p1 = Person("John", 36)
print("Hello my name is " + p1.getName())