''' Visualization of Square integers using Matplotlib. From Chaper 15 of Python Crash Course 2nd Edition by Eric Matthes'''

import matplotlib.pyplot as plt
# print(plt.style.available)

input_values = range(1, 11)
squares = [x ** 2 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()
