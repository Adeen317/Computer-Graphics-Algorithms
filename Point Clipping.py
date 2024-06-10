import matplotlib.pyplot as plt
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = 0
    if x < xmin:
        code |= 1
    elif x > xmax:
        code |= 2
    if y < ymin:
        code |= 4
    elif y > ymax:
        code |= 8
    return code

def point_clip(x, y, xmin, ymin, xmax, ymax):
    code = compute_code(x, y, xmin, ymin, xmax, ymax)

    if code == 0:
        return "Visible"

    for i in range(4):
        if code & (1 << i):
            return "Invisible"
    return "Visible"

def main():
    xmin = int(input("Enter xmin of clipping region: "))
    ymin = int(input("Enter ymin of clipping region: "))
    xmax = int(input("Enter xmax of clipping region: "))
    ymax = int(input("Enter ymax of clipping region: "))

    x = int(input("Enter x coordinate of the point: "))
    y = int(input("Enter y coordinate of the point: "))

    print("Point clipping status:", point_clip(x, y, xmin, ymin, xmax, ymax))

    # Plot the clipping window
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r-', label='Clipping Window')

    # Plot the point
    plt.plot(x, y, 'bo', label='Point')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Point Clipping')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
