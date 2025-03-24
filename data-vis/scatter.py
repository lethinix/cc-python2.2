import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
y = [5, 15, 10, 20, 18, 25, 30, 22, 28, 35]  

sizes = [value * 10 for value in y]  #easy way to create a new array in python based on another array
colors = x  

plt.scatter(x, y, c=colors, s=sizes, cmap='viridis', alpha=0.7) #cmap stands for color map
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.colorbar(label="Color Scale")
plt.show()