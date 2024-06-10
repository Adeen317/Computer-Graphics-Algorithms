import matplotlib.pyplot as plt

# Global variable to store the ellipse points
ellipse_points = []

def setPixel(x, y):
    ellipse_points.append((x, y))

def ellipseMidpoint(xCenter, yCenter, Rx, Ry):
    Rx2 = Rx * Rx
    Ry2 = Ry * Ry
    twoRx2 = 2 * Rx2
    twoRy2 = 2 * Ry2
    p = 0
    x = 0
    y = Ry
    px = 0
    py = twoRx2 * y
    # Define a function to plot the ellipse points
    def ellipsePlotPoints(xCenter, yCenter, x, y):
        setPixel(xCenter + x, yCenter + y)
        setPixel(xCenter - x, yCenter + y)
        setPixel(xCenter + x, yCenter - y)
        setPixel(xCenter - x, yCenter - y)
    ellipsePlotPoints(xCenter, yCenter, x, y)
    p = round(Ry2 - (Rx2 * Ry) + (0.25 * Rx2))
    while px < py:
        x += 1
        px += twoRy2
        if p < 0:
            p += Ry2 + px
        else:
            y -= 1
            py -= twoRx2
            p += Ry2 + px - py
        ellipsePlotPoints(xCenter, yCenter, x, y)
    p = round(Ry2 * (x + 0.5) * (x + 0.5) + Rx2 * (y - 1) * (y - 1) - Rx2 * Ry2)
    while y > 0:
        y -= 1
        py -= twoRx2
        if p > 0:
            p += Rx2 - py
        else:
            x += 1
            px += twoRy2
            p += Rx2 - py + px
        ellipsePlotPoints(xCenter, yCenter, x, y)
    return ellipse_points
# Define the ellipse parameters
xCenter = 0
yCenter = 0
Rx = 30
Ry = 10
# Generate the ellipse points using the Midpoint Ellipse Algorithm
ellipse_points = ellipseMidpoint(xCenter, yCenter, Rx, Ry)
# Unzip the ellipse points for plotting
x_coords, y_coords = zip(*ellipse_points)
# Plot the generated ellipse
plt.figure()
plt.plot(x_coords, y_coords, 'bo')  # 'bo' stands for blue color and circle marker
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Ellispe Algorithm")
plt.show()
