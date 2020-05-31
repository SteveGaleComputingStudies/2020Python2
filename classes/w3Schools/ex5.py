# https://www.w3schools.com/python/python_classes.asp
# w3 schools example with get and set methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):
    return(self.name)

  def getAge(self):
      return(self.age)

  def setAge(self,age):
      self.age = age

p1 = Person("John", 36)
print("Hello my name is " + p1.getName())
p1.setAge(21)
print("My age is now {}".format( p1.getAge()))