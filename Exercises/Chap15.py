from random_walk import RandomWalk
import matplotlib.pyplot as plt

# ! 15-1 - A number raised to the thir power is a cube. Plot the first five cubic numbers, and then plot the first 5000 numbers
# ! 15-2 - Apply a colormap to your cubes plot

input_nums = range(1, 5000)
values = [x**3 for x in input_nums]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_nums, values, c=values, cmap=plt.cm.plasma, s=10)

ax.set_title('Cubes', fontsize=24)
ax.set_ylabel('Values of Cubes', fontsize=14)
ax.set_xlabel('Values', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# ! 15-3 - modify rw_visual to use ax.plot instead of ax.scatter.
# ! 15-4 - modify random_walk to add more distances to the list or remove the -1 from the direction of x or y.
# ! 15-5 - refactor the random_walk method to make it less lengthy.


rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=2)
plt.show()
