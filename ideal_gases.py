
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#P = np.linspace(0.01, 1000, 500)
V = np.linspace(1, 50, 500)
T = np.linspace(1, 300, 500)

n = 1.
R = 0.0821

fig = plt.figure(1, figsize = (10,6))
ax = fig.add_subplot(111, projection='3d')

V, T = np.meshgrid(V,T)
Z = R*T/V

ax.plot_wireframe(V, T, Z, rstride=50, cstride=50)

ax.set_xlabel('Volume')
ax.set_ylabel('Temperature')
ax.set_zlabel('Pressure')

# plt.show()
# rotate the axes and update

for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

