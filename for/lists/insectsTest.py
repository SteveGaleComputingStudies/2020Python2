insects = ["ant","beetle","bug","mayfly"]

print(insects)
for x in insects:
    print(x + " : " + str(insects.index(x)))
    #print(insects.index(x))
    print(" {0} : {1}".format(x,insects.index(x))) 