''' Visualization of random connected points using Matplotlib. From Chaper 15 of Python Crash Course 2nd Edition by Eric Matthes'''

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(80_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))

points_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=points_numbers,
           cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.set_aspect('equal')

# emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1],
           c='red', edgecolors='none', s=100)

# Remove axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

# ! Make a while loop if you want to generate many plots.
# keep_running = input('Make another walk (y/n)? ')
# if keep_running == 'n':
#     break
