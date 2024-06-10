import matplotlib.pyplot as plt

# Define region codes 
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region 
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Function to clip the line segment 
def cohen_sutherland_line_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        # If both endpoints lie inside the rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # If both endpoints are outside the rectangle and in same region
        elif code1 & code2:
            break
       # Some portion of the line is inside the rectangle
        else:
            x = 0
            y = 0
            code_out = code1 if code1 else code2

            # Find intersection point using clip rectangle borders
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        return [(x1, y1), (x2, y2)]
    else:
        return None

def plot_clipping_window(xmin, ymin, xmax, ymax):
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r-', label='Clipping Window')

def plot_line(x1, y1, x2, y2, color='b', label='Line'):
    plt.plot([x1, x2], [y1, y2], color=color, label=label)

def main():
    xmin = int(input("Enter xmin of clipping region: "))
    ymin = int(input("Enter ymin of clipping region: "))
    xmax = int(input("Enter xmax of clipping region: "))
    ymax = int(input("Enter ymax of clipping region: "))
   
    x1 = int(input("Enter x1 coordinate of the line: "))
    y1 = int(input("Enter y1 coordinate of the line: "))
    x2 = int(input("Enter x2 coordinate of the line: "))
    y2 = int(input("Enter y2 coordinate of the line: "))
    
    clipped_line = cohen_sutherland_line_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    if clipped_line:
        print("Line clipping status: Visible")
        plt.figure()
        plot_clipping_window(xmin, ymin, xmax, ymax)
        plot_line(x1, y1, x2, y2)
        clipped_x1, clipped_y1 = clipped_line[0]
        clipped_x2, clipped_y2 = clipped_line[1]
        plot_line(clipped_x1, clipped_y1, clipped_x2, clipped_y2, color='g', label='Clipped Line')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Cohen-Sutherland Line Clipping')
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
    else:
        print("Line clipping status: Invisible")

if __name__ == "__main__":
    main()
