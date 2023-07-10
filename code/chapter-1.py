import os
import matplotlib.pyplot as plt

# Create data and output folder if they don't exist
data_folder = 'data'
output_folder = 'output'

if not os.path.exists(data_folder):
  os.mkdir(data_folder)
if not os.path.exists(output_folder):
  os.mkdir(output_folder)

points = [(0.1, 0.5), (0.5, 0.5), (0.9, 0.5)]

# Zip the points list to x and y to be used in the plot method
x, y = zip(*points)

# Create a figure and an axis
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(5, 5)
ax.plot(x, y, color='green', marker='o', linestyle='None')

# Save figure as a .png file to the output directory
output_path = os.path.join(output_folder, 'simple.png')
plt.savefig(output_path)

# Draw the plot
plt.show()


