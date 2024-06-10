import matplotlib.pyplot as plt
import numpy as np

def multiview_projection(cube, matrix):
    viewed_matrix = np.dot(matrix, cube)
    return viewed_matrix

# Define the cube vertices and projection matrices
cube = np.array([[0, 1, 1, 0, 0, 1, 1, 0],  # x-coordinates
                 [0, 0, 1, 1, 0, 0, 1, 1],  # y-coordinates
                 [0, 0, 0, 0, 1, 1, 1, 1],  # z-coordinates
                 [1, 1, 1, 1, 1, 1, 1, 1]]) # homogeneous coordinates

# Define the translation matrix for 50 units along the y-axis
translation_y = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 50],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

# Define the translation matrix for 100 units along the z-axis
translation_z = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 100],
                        [0, 0, 0, 1]])

# Apply the translations to the cube
translated_cube_y = np.dot(translation_y, cube)
translated_cube_z = np.dot(translation_z, cube)

# Edges of the cube
edges = [(0, 1), (1, 2), (2, 3), (3, 0),  # bottom face
         (4, 5), (5, 6), (6, 7), (7, 4),  # top face
         (0, 4), (1, 5), (2, 6), (3, 7)]  # vertical lines

# Plot the original and translated cubes
fig = plt.figure(figsize=(15, 10))

# Original 3D points with edges
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
for edge in edges:
    ax1.plot([cube[0, edge[0]], cube[0, edge[1]]],
             [cube[1, edge[0]], cube[1, edge[1]]],
             [cube[2, edge[0]], cube[2, edge[1]]], 'b')
ax1.set_title("Original 3D")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Translated cube along y-axis with edges
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
for edge in edges:
    ax2.plot([translated_cube_y[0, edge[0]], translated_cube_y[0, edge[1]]],
             [translated_cube_y[1, edge[0]], translated_cube_y[1, edge[1]]],
             [translated_cube_y[2, edge[0]], translated_cube_y[2, edge[1]]], 'g')
ax2.set_title("Translated along Y")
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# Translated cube along z-axis with edges
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
for edge in edges:
    ax3.plot([translated_cube_z[0, edge[0]], translated_cube_z[0, edge[1]]],
             [translated_cube_z[1, edge[0]], translated_cube_z[1, edge[1]]],
             [translated_cube_z[2, edge[0]], translated_cube_z[2, edge[1]]], 'r')
ax3.set_title("Translated along Z")
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
