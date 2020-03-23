index = 0
toAverage = int(input(" enter how many scores to average"))
sum = 0
while (index < toAverage):
    value = int(input("enter a score"))
    sum = sum  + value
    index = index + 1

average = sum / index
print("average = {0:.2f}".format(average))
