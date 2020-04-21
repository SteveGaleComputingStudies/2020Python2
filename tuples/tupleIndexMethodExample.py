#2020 tuple methods example
thistuple = ("apple", "banana", "cherry", "banana")
print("index of banana",thistuple.index("banana"))  # = 1
print("count of banana",thistuple.count("banana"))  # = 2

#string methods example
str = "banana"
str.lower()

#find the index of the second banana in the tuple
print("index of banana",thistuple.index("banana",2,4))  # = 3

#index the tuple
print(thistuple[1]) # = "banana"

#use a for loop to iterate through the tuple
print("iterate in loop")
for i in range(0,4):
    print(thistuple[i])

#find the index and use it
appleIndex = thistuple.index("apple") # = 0 
print(thistuple[appleIndex]) # thistuple[0]
print()
for i in range(0,len(thistuple)):
    print(thistuple[i])

# for x in insects:
#   print(x + insects.index(x))
#   print(insects.index(x))



