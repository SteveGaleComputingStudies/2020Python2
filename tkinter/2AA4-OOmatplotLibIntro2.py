import matplotlib.pyplot as plt


fig, ax = plt.subplots()  #  a figure containing an axes.
#plot of y = x^2

ax.plot([1, 2, 3, 4], [1, 2, 3, 4], label='linear')  # Plot some data on the (implicit) axes.
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label='quadratic')  # etc.
ax.plot([1, 2, 3, 4], [1, 8, 27, 64], label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()
plt.show()
