import matplotlib.pyplot as plt

def plot_circle_points(x_center, y_center, x, y, x_values, y_values):
    points = [
        (x_center + x, y_center + y),
        (x_center - x, y_center + y),
        (x_center + x, y_center - y),
        (x_center - x, y_center - y),
        (x_center + y, y_center + x),
        (x_center - y, y_center + x),
        (x_center + y, y_center - x),
        (x_center - y, y_center - x)
    ]
    for point in points:
        x_values.append(point[0])
        y_values.append(point[1])

def circle(x_center, r):
    x = 0
    y = r
    p = 1 - r
    x_values = []
    y_values = []

    plot_circle_points(x_center, x_center, x, y, x_values, y_values)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x + 1 - 2 * y

        plot_circle_points(x_center, x_center, x, y, x_values, y_values)

    plt.scatter(x_values, y_values)
    plt.title('Circle Drawing Algorithm')
    plt.axis('equal')  # Ensure the circle is not skewed
    plt.show()

circle(0, 20)
