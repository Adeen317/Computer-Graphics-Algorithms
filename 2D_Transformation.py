import numpy as np
import matplotlib.pyplot as plt

def transformation(y, x):
    transform=np.dot(x,y)
    return transform


tri_x = np.array([[0, 5, 0, 0],
                  [0,0,5,0]])

rotation=np.array([[0.707, -0.707],
                   [0.707, 0.707]])

scaling=np.array([[2, 0],
                  [0, 2]])

translation=np.array([[1,0],
                     [0,0]])


t_rot = transformation(tri_x, rotation)
t_sca=transformation(tri_x, scaling)
t_tra=transformation(tri_x, translation)


# Plot the original triangle
plt.plot(tri_x[0], tri_x[1], 'b-', label='Original Triangle')

# Plot the translated triangle
plt.plot(t_tra[0], t_tra[1], 'o-', label='Translated Triangle')

# Plot the scaled triangle
plt.plot(t_sca[0], t_sca[1], 'g-', label='Scaled Triangle')

# Plot the transformed triangle
plt.plot(t_rot[0], t_rot[1], 'r-', label='Transformed Triangle')

# Set plot labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Transformation')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()

# Plot the transformed triangle
plt.plot(t[0], t[1], 'r-', label='Transformed Triangle')

# Set plot labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Transformation')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()

# Plot the transformed triangle
plt.plot(t[0], t[1], 'r-', label='Transformed Triangle')

# Set plot labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Transformation')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()
