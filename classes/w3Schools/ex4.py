class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def getName(self):          #getmethod for instance variable
    return(self.name)

  def setName(self,name):     #set method fro name instance variable
    self.name = name

  def getAge(self):          #getmethod for instance variable
    return(self.age)

  def setAge(self,age):     #set method fro name instance variable
    self.age = age

p1 = Person("John", 36)
print("Hello my name is " + p1.getName())


p1.setAge(37)

print("{0} age is {1}".format(p1.getName(),p1.getAge()))