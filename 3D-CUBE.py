'''This code creates a figure and adds a 3D plot to it. It 
then defines the vertices of the cube and plots them as 
scattered points. Finally, it connects the vertices to form 
the faces of the cube and displays the plot.'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Plot the vertices of the cube
ax.scatter(x, y, z)

# Connect the vertices to form the faces of the cube
for i in range(4):
    ax.plot([x[i], x[i+4]], [y[i], y[i+4]], [z[i], z[i+4]])
    ax.plot([x[i], x[(i+1)%4]], [y[i], y[(i+1)%4]], [z[i], z[(i+1)%4]])
    ax.plot([x[i+4], x[4+(i+1)%4]], [y[i+4], y[4+(i+1)%4]], [z[i+4], z[4+(i+1)%4]])

# Show the plot
plt.show()
