import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the triangle
vertices = np.array([[-1, 6], [2, 0], [-4, 9]])

# Define the rotation angle in degrees
rotation_angle = -45

# Define the rotation matrix
theta = np.radians(rotation_angle)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

# Rotate the vertices of the triangle
rotated_vertices = np.dot(vertices, rotation_matrix.T)

# Extract x and y coordinates from rotated vertices
x_rotated = rotated_vertices[:, 0]
y_rotated = rotated_vertices[:, 1]

for i in range(3):
    plt.plot([x_rotated[i], x_rotated[(i + 1) % 3]], [y_rotated[i], y_rotated[(i + 1) % 3]], 'r-')

plt.plot(x_rotated, y_rotated, 'bo')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Rotated Triangle')
plt.axis('equal')
plt.grid(True)
plt.show()
