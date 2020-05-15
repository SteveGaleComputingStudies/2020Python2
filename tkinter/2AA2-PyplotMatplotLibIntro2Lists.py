import matplotlib.pyplot as plt

xList = [1, 2, 3, 4]
linearList = xList
quadList = [1, 4, 9, 16]
cubList = [1, 8, 27, 64]

#plt.plot([xvalues],[yvalues],options='..')
plt.plot(xList, xList, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(xList,quadList, label='quadratic')  # etc.
plt.plot(xList, cubList, label='cubic')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Simple Plot of linear , quadratic etc")
plt.legend()
plt.show()