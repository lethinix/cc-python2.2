import matplotlib.pyplot as plt

x = ["a", "b", "c", "d", "e"]
y = [10, 20, 25, 30, 40]
colors = ["red", "green", "blue", "orange", "purple"]
plt.bar(x, y, color=colors, label='bar chart')
plt.xlabel("categories")
plt.ylabel("values")
plt.title("my first chart")
plt.legend()
plt.show()

