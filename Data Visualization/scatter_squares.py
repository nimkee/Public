import matplotlib.pyplot as plt
from pathlib import Path

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')

fig, ax = plt.subplots()

#Set chart title and label axes
#ax.scatter(x_values, y_values, color='green', s=10)
#Alternatively can set the color using RGB, with the syntax:
#ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(labelsize=14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

#plt.show()

#desktop = Path('C:/Users/nimke/Desktop/squares_plot.png')


plt.savefig('squares_plot.png', bbox_inches='tight')