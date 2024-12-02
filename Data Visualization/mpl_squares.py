import matplotlib.pyplot as plt
plt.style.available

input_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)

# Set chart title and label axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of the tick labels
ax.tick_params(labelsize=14)

plt.show()