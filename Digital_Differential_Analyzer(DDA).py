import matplotlib.pyplot as plt

def DDA(x1,y1,x2,y2):
    dx= x2-x1
    dy=y2-y1
    steps= max(abs(dx),abs(dy))
    xinc=dx/steps
    yinc=dy/steps
    x=x1
    y=y1
    x_values=[]
    y_values=[]
    for i in range(steps):
        x_r=round(x)
        y_r=round(y)
        print(f"({x_r},{y_r})")
        x_values.append(x_r)
        y_values.append(y_r)
        x+=xinc
        y+=yinc
    
    plt.plot(x_values,y_values,marker="o",color='blue')
    plt.title("DDA Line Algorithm")
    plt.show()
           
DDA(1,1,4,7)
