class Person:
  def __init__(self, name, age):      # constructor - constructs object from class spec initialising the instance variables
    self.name = name                  # instance variable name
    self.age = age                    # instance variable age

p1 = Person("John", 36)               # object p1 of type class Person
p2 = Person("Bill", 23)               # object p2 of type class Person
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


p2.age = 24
print(p2.age)