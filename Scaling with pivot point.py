import numpy as np
import matplotlib.pyplot as plt

def transformation(y, x):
    transform=np.dot(x,y)
    return transform


tri = np.array([[0, 5, 0, 0],
                  [0, 0, 5, 0]])

scaling=np.array([[2, 0],
                  [0, 2]])
x=int(input("Enter the x-coordinate of the translation: "))
y=int(input("Enter the y-coordinate of the translation: "))


translation=np.array([[x],[y]])


t_tra=(tri + translation)
new=transformation(t_tra, scaling)


# Plot the original triangle
plt.plot(tri[0], tri[1], 'b-', label='Original Triangle')

# Plot the transformed triangle
plt.plot(new[0], new[1], 'y-', label='Transformed Triangle')

# Set plot labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Transformation')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()
