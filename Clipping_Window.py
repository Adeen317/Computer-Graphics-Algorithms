import matplotlib.pyplot as plt

def scale_point(point, window_size):
    return (point[0] / window_size[0], point[1] / window_size[1])

def map_to_normalized_viewport(polygon, clipping_window_size):
    normalized_polygon = [scale_point(point, clipping_window_size) for point in polygon]
    return normalized_polygon

def map_to_device_window(polygon, device_window_size):
    device_polygon = [(point[0] * device_window_size[0], point[1] * device_window_size[1]) for point in polygon]
    return device_polygon

# Given data
clipping_window_size = (800, 600)
polygon = [(300, 100), (500, 100), (500, 400), (400, 500), (300, 400)]
normalized_viewport_size = (1, 1)
device_window_size = (640, 480)

# Map polygon to the normalized viewport
normalized_polygon = map_to_normalized_viewport(polygon, clipping_window_size)
print("Normalized viewport polygon:", normalized_polygon)

# Map polygon to the device window
device_polygon = map_to_device_window(normalized_polygon, device_window_size)
print("Device window polygon:", device_polygon)

# Create subplots for clipping window and device window polygons
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot the clipping window polygon
x, y = zip(*polygon)
ax1.plot(x, y, label='Clipping Window Polygon')
ax1.set_title('Clipping Window Polygon')
ax1.set_aspect('equal', adjustable='box')

# Plot the device window polygon
x_device, y_device = zip(*device_polygon)
ax2.plot(x_device, y_device, label='Device Window Polygon')
ax2.set_title('Device Window Polygon')
ax2.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()
