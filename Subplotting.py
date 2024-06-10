import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,6))

#first subplot
axs1 = fig.add_subplot(1, 2, 1)
axs1.plot(((0, 3), (1, 8), (2, 1), (3, 10)))
axs1.set_title("Plot 1")
axs1.set_xlabel("x axis")
axs1.set_ylabel("y axis")

#second subplot
axs2 = fig.add_subplot(1, 2, 2)
axs2.plot(((0, 10), (1, 20), (2, 30), (3, 40)))
axs2.set_title("Plot 2")
axs2.set_xlabel("x axis")
axs2.set_ylabel("y axis")

fig.show()
