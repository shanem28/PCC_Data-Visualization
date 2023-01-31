''' Visualization of Dice rolls using Plotly. From Chaper 15 of Python Crash Course 2nd Edition by Eric Matthes'''

from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)
die_2 = Die(8)

data = []
# Added a loop to run multiple simulations if desired.
for _ in range(1):
    results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result+1)]

    x_values = list(range(2, max_result+1))
    data.append(Bar(x=x_values, y=frequencies))

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D8 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='HTML/d8_d8.html')
