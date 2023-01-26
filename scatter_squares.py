''' Visualization of Scatter Squares using Matplotlib. From Chaper 15 of Python Crash Course 2nd Edition by Eric Matthes'''

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Specify scatter point colors. You can specify a color, or RGB, or a colormap

# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, color=[0,0.8,0], s=10)

# ! Find more colormaps here https://matplotlib.org/stable/gallery/color/colormap_reference.html
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axis
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

fig.savefig('IMAGES/squares_plot1.png', bbox_inches='tight')
plt.show()

# This will save any changes made when in the pyplot interface
fig.savefig('IMAGES/squares_plot2.png', bbox_inches='tight')
