import numpy as np
import matplotlib.pyplot as plt
import math
geometry = np.array([[1,0],[1,5],[5,0],[1,0]])
plt.plot(geometry[:,0],geometry[:,1])
plt.grid()
plt.title("Original Geometry")
plt.show()
tx,ty=geometry[0]
geometry=np.transpose(geometry)
homogenous_row=np.array([1,1,1,1])
geometry=np.append(geometry,[homogenous_row],axis=0)
angle=45;
neg_translation=np.array([[1,0,-tx],
[0,1,-ty],
[0,0,1]])
rotation = np.array([[np.cos(math.radians(angle)), -np.sin(math.radians(angle)), 0],
 [np.sin(math.radians(angle)), np.cos(math.radians(angle)), 0],
 [0, 0, 1]])
pos_translation=np.array([[1,0,tx],
[0,1,ty],
[0,0,1]])
neg_trans_rot=np.dot(neg_translation,rotation)
CM=np.dot(neg_trans_rot,pos_translation)
rotated_geometry=np.dot(CM,geometry)
plt.plot(rotated_geometry[0,:],rotated_geometry[1,:])
plt.grid()
plt.title("Rotated Geometry")
plt.show()
