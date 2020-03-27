import matplotlib.pyplot as plt
plt.scatter(2, 4)
plt.scatter(3, 6)
plt.scatter(1, 1)
plt.scatter(4, 5)
plt.scatter(7, 3)
plt.scatter(2, 4, s=200)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.scatter(x_values, y_values, edgecolor='none', s=40)
plt.scatter(x_values, y_values, s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()