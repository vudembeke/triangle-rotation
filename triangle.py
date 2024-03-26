import matplotlib.pyplot as plt

# Define the vertices of the triangle
vertices = [(-1, 6), (2, 0), (-4, 9)]

# Extract x and y coordinates from vertices
x = [vertex[0] for vertex in vertices]
y = [vertex[1] for vertex in vertices]

# Plot the triangle
plt.figure()
plt.plot(x + [x[0]], y + [y[0]], 'r-')  # Connect the vertices to form the triangle
plt.plot(x, y, 'bo')  # Plot the vertices
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle')
plt.grid(True)
plt.axis('equal')
plt.show()
