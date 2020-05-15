import matplotlib.pyplot as plt

#plt.plot([xvalues],[yvalues],options='..')
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label='linear')  # Plot some data on the (implicit) axes.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label='quadratic')  # etc.
plt.plot([1, 2, 3, 4], [1, 8, 27, 64], label='cubic')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Simple Plot of linear , quadratic etc")
plt.legend()
plt.show()