import numpy as np
import matplotlib.pyplot as plt
import matplotlib

fig = plt.figure(1,(8,8))
ax = fig.add_subplot(111)

ax.set_aspect('equal', 'datalim')

plt.xkcd()
plt.axis('off')

xmin, xmax, ymin, ymax = 0, 3, 0, 3

plt.plot([0,3,3,0,0],[0,0,3,3,0], color='b')
#plt.plot([0,3],[1,1], color='b')
#plt.plot([0,3],[2,2], color='b')
#plt.plot([1,1],[0,3], color='b')
#plt.plot([2,2],[0,3], color='b')

ax.fill([0,3,3,0], [0,0,3,3])                    # a polygon with default color

plt.plot(1,1, 'go', color='r')                 # Additional point
plt.plot(2,1, 'go', color='r')                 # Additional point
plt.plot(1,2, 'go', color='r')                 # Additional point
plt.plot(2,2, 'go', color='r')                 # Additional point

plt.plot(0,1, 'go', color='r')                 # Additional point
plt.plot(0,2, 'go', color='r')                 # Additional point
plt.plot(3,1, 'go', color='r')                 # Additional point
plt.plot(3,2, 'go', color='r')                 # Additional point
plt.plot(1,0, 'go', color='r')                 # Additional point
plt.plot(2,0, 'go', color='r')                 # Additional point
plt.plot(1,3, 'go', color='r')                 # Additional point
plt.plot(2,3, 'go', color='r')                 # Additional point

font = {'size'   : 22}

matplotlib.rc('font', **font)

eps=0.1
ax.text(1, 2+eps, r'$x_1$')
ax.text(2, 2+eps, r'$x_2$')
ax.text(1, 1+eps, r'$x_4$')
ax.text(2, 1+eps, r'$x_3$')

eps=-0.5
ax.text(0+eps, 2, r'$10^\circ\mathrm{C}$', size='20')
ax.text(0+eps, 1, r'$10^\circ\mathrm{C}$')
eps=0.05
ax.text(3+eps, 2, r'$40^\circ\mathrm{C}$')
ax.text(3+eps, 1, r'$40^\circ\mathrm{C}$')

eps=0.05
ax.text(1, 3+eps, r'$20^\circ\mathrm{C}$')
ax.text(2, 3+eps, r'$20^\circ\mathrm{C}$')
eps=0.2
ax.text(1, 0-eps, r'$30^\circ\mathrm{C}$')
ax.text(2, 0-eps, r'$30^\circ\mathrm{C}$')


plt.savefig("deska.svg")
plt.savefig("deska.png")
