import matplotlib.pyplot as plt
def bresenham(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dy2=2*dy
    p=dy2-dx
    y=y1
    
    x_coordinates=[]
    y_coordinates=[]
    
    for x in range (x1,x2+1):
        print("(",x,",",y,")")
        if(p<0):
            p=p+dy2
        else:
            y=y+1
            p=p+dy2-(2*dx)
            print(f"({x},{y})")
        print(f"({x},{y})")
        x_coordinates.append(x)
        y_coordinates.append(y)
    plt.plot(x_coordinates,y_coordinates,marker="o")
    plt.title("Bresenham's Algorithm")
    plt.show()
bresenham(10,20,15,30)
