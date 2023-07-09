import os
import matplotlib.pyplot as plt

data_folder = 'data'
output_folder = 'output'

if not os.path.exists(data_folder):
  os.mkdir(data_folder)
if not os.path.exists(output_folder):
  os.mkdir(output_folder)

points = [(0.1, 0.5), (0.5, 0.5), (0.9, 0.5)]

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(5, 5)

ax.plot(*point, color='green', marker='o')

plt.show()


