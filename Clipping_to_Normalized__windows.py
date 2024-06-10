import matplotlib.pyplot as plt
import numpy as np

polygon = [[300, 500, 500, 400, 300, 300], [100, 100, 400, 500, 400, 100],[0, 0, 0, 0, 0, 1]]

XVmn = 0
YVmn = 0
XVmx = 1
YVmx = 1
XWmn = 0
YWmn = 0
XWmx = 800
YWmx = 600
DVPx = 640
DVPy = 480
Sx = ((XVmx - XVmn) / (XWmx - XWmn))
Sy = ((YVmx - YVmn) / (YWmx - YWmn))
Tx = ((XWmx * XVmn) - (XWmn * XVmn)) / (XWmx - XWmn)
Ty = ((YWmx * YVmn) - (YWmn * YVmn)) / (YWmx - YWmn)
CM = [[Sx, 0, Tx],[0, Sy, Ty],[0, 0, 1]]
NM = np.dot(CM, polygon)
DPx = [x * DVPx for x in NM[0]]
DPy = [y * DVPy for y in NM[1]]
plt.plot(polygon[0], polygon[1])
plt.title("Clipping Window")
plt.figure()
plt.plot(NM[0], NM[1])
plt.title("Normalized Viewport")
plt.figure()
plt.plot(DPx, DPy)
plt.title("Device Viewport")
plt.show()
