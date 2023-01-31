''' Visualization of Dice rolls using Plotly. From Chaper 15 of Python Crash Course 2nd Edition by Eric Matthes'''

import plotly.express as px

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

title = 'Results of rolling two D8 50,000 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()
