#2020 tuple methods example
thistuple = ("apple", "banana", "cherry", "banana")
print("index of banana",thistuple.index("banana"))
print("count of banana",thistuple.count("banana"))

#string methods example
str = "banana"
str.lower()

#find the index of the second banana in the tuple
print("index of banana",thistuple.index("banana",2,4))

#index the tuple
print(thistuple[1])

#use a for loop to iterate through the tuple
for i in range(0,4):
    print(thistuple[i])

#find the index and use it
appleIndex = thistuple.index("apple")
print(thistuple[appleIndex])
