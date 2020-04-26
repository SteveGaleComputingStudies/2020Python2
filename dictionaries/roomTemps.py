
roomTemps = {'Room': ['E223','E222','E208','E219'],
        'Temperature': [22.1,21.4,23.5,22.6]
        }


print("Room", end='\t')
for room in roomTemps['Room']:                  # array indexing
    print("{0}".format(room), end='\t')
print()
print("Temp", end='\t')
for temp in roomTemps['Temperature']:          # array indexing
    print("{0}".format(temp), end='\t')