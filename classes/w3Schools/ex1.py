class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)

p2.x = 2
p1.x = 1

print(p1.x)
print(p2.x)