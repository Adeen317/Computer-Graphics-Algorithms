#SutherlandHodgmanAlgorithm
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def clip_polygon(polygon, clip_rect):
    def inside(p, edge):
        if edge == 'left':
            return p[0] >= clip_rect[0][0]
        elif edge == 'right':
            return p[0] <= clip_rect[1][0]
        elif edge == 'bottom':
            return p[1] >= clip_rect[0][1]
        elif edge == 'top':
            return p[1] <= clip_rect[1][1]

    def intersect(p1, p2, edge):
        if edge in ['left', 'right']:
            x = clip_rect[0][0] if edge == 'left' else clip_rect[1][0]
            y = p1[1] + (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0])
            return (x, y)
        elif edge in ['bottom', 'top']:
            y = clip_rect[0][1] if edge == 'bottom' else clip_rect[1][1]
            x = p1[0] + (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1])
            return (x, y)

    edges = ['left', 'right', 'bottom', 'top']
    for edge in edges:
        new_polygon = []
        for i in range(len(polygon)):
            current_point = polygon[i]
            prev_point = polygon[i - 1]
            if inside(current_point, edge):
                if not inside(prev_point, edge):
                    new_polygon.append(intersect(prev_point, current_point, edge))
                new_polygon.append(current_point)
            elif inside(prev_point, edge):
                new_polygon.append(intersect(prev_point, current_point, edge))
        polygon = new_polygon
    return polygon

# Define the original polygon vertices
polygon = [(9, -3), (18, 4), (7, 10)]

# Define the clipping rectangle as ((x_min, y_min), (x_max, y_max))
clip_rect = ((0, 0), (15, 8))

# Perform the clipping
clipped_polygon = clip_polygon(polygon, clip_rect)

# Plotting the original polygon
fig, ax = plt.subplots()
polygon_patch = patches.Polygon(polygon, closed=True, fill=True, edgecolor='r', facecolor='r', alpha=0.3)
ax.add_patch(polygon_patch)

# Plotting the clipping region
clip_rect_patch = patches.Rectangle(clip_rect[0], clip_rect[1][0] - clip_rect[0][0], clip_rect[1][1] - clip_rect[0][1],
                                    fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(clip_rect_patch)

# Plotting the clipped polygon
if clipped_polygon:
    clipped_polygon_patch = patches.Polygon(clipped_polygon, closed=True, fill=True, edgecolor='g', facecolor='g', alpha=0.5)
    ax.add_patch(clipped_polygon_patch)

# Setting the plot limits
ax.set_xlim(-5, 20)
ax.set_ylim(-5, 15)

# Adding labels and title
ax.set_title('Sutherland-Hodgman Polygon Clipping')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

plt.gca().set_aspect('equal', adjustable='box')
plt.legend(['Original Polygon', 'Clipping Region', 'Clipped Polygon'])
plt.show()
