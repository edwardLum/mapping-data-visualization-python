import os
import matplotlib.pyplot as plt

# Create data and output folder if they don't exist
data_folder = 'data'
output_folder = 'output'

if not os.path.exists(data_folder):
  os.mkdir(data_folder)
if not os.path.exists(output_folder):
  os.mkdir(output_folder)

point1 = (4, 1)
point2 = (3, 4)

# Create a figure and an axis
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(5, 5)
ax.plot(*point1, color='green', marker='^')
ax.plot(*point2, color='red', marker='o')

# Save figure as a .png file to the output directory
output_path = os.path.join(output_folder, 'exercise1.png')
plt.savefig(output_path)

# Draw the plot
plt.show()


