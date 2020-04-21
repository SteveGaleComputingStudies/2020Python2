thislist = ["apple", "cherry", "banana"]
mylist = thislist.copy()
originalList = thislist # refeence to thislist
print(mylist)
thislist.sort()
print(thislist)
print(mylist)
print(originalList)
originalList.pop()
print(thislist)