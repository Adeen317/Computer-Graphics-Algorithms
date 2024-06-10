import matplotlib.pyplot as plt

def create_circle(radius, xc, yc):
    points = set()

    x0, y0 = 0, radius
    x, y = x0, y0
    p = 5/4 - radius
    k = 0

    def plot_points(xc, yc, x, y):
        points.add((xc + x, yc + y))
        points.add((xc - x, yc + y))
        points.add((xc + x, yc - y))
        points.add((xc - x, yc - y))
        points.add((xc + y, yc + x))
        points.add((xc - y, yc + x))
        points.add((xc + y, yc - x))
        points.add((xc - y, yc - x))

    while x <= y:
        plot_points(xc, yc, x, y)
        if p < 0:
            p += 2*x + 1
        else:
            p += 2*(x - y) + 1
            y -= 1
        x += 1

    return points

def check_point_position(x, y, radius):
    fx_y = x**2 + y**2 - radius**2
    if fx_y < 0:
        return "Inside"
    elif fx_y > 0:
        return "Outside"
    else:
        return "On the circle"

# Circle parameters
radius = 50
xc, yc = 0, 0

# Create the circle
circle_points = create_circle(radius, xc, yc)

# Check a point
x_point, y_point = 20, 30
position = check_point_position(x_point, y_point, radius)

# Plot the circle and the point
fig, ax = plt.subplots()
for point in circle_points:
    ax.plot(point[0], point[1], 'bo')  # Plot circle points in blue color

ax.plot(x_point, y_point, 'ro')  # Plot the test point in red color
ax.annotate(f'({x_point}, {y_point}): {position}', (x_point, y_point + 3))  # Annotate the position of the point

plt.title("Midpoint Circle Algorithm")
ax.set_aspect('equal', adjustable='datalim')
plt.gca().set_aspect('equal', adjustable='box')
plt.gca().invert_yaxis()
plt.show()
