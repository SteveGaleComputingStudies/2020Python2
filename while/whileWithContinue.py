counter = 0 
while (counter < 20):
    counter = counter + 1
    if (counter % 2 == 0):  #test for even
        continue
    print(counter)
    if (counter > 10):
        break