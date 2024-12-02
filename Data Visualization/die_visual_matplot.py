from die import Die
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

#Create a D6

die_1 = Die(8)
die_2 = Die(8)

#Make some rolls, store results in a list

results = []
#Can I write this as a list comprehension?
for roll_num in range(50_000):
    results.append(die_1.roll() + die_2.roll())
    #could split the addition and append line up separately

# List comprehension --> results = [die_1.roll()+die_2.roll() for roll_num in range(50_000)]
#Can I write this as a list comprehension?

#Analyze the results

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1) #because it is UP TO the second number

frequencies = [results.count(value) for value in poss_results]
"""for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency) #Or could combine these two lines into one"""

# Visualize the results
title = f"Results of Rolling a D{die_1.num_sides} and a D{die_2.num_sides} 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Results'}

#Plot


fig, ax = plt.subplots()

ax.bar(poss_results, frequencies, width=1, edgecolor='white', linewidth=.7, label=title)

ax.axis([2, max_result+1, 0, 10000])
plt.show()