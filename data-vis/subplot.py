import matplotlib.pyplot as plt
import pandas as plt

fig, ax = plt.subplots(1, 2, figsize=(10,5))
ax[0].bar(["a,", "b", "c"], [10, 20, 15], color='blue')
ax[0].set_title("chart 1")
plt.xlabel("day of the week")
plt.ylabel("how many hours slept")

# Second subplot (Line chart)
ax[1].plot(["thursday", "friday", "saturday", "sunday"], [10, 8, 9, 9], marker='*', color=('#33E3FF'))
ax[1].set_title("sleeping chart")
ax[1].set_facecolor('black')

plt.show()