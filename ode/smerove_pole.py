from pylab import *
from numpy import ma
from matplotlib import mlab
from scipy.integrate import odeint

plt.xkcd()

fig = figure(figsize=(8,8))
ax = fig.add_subplot(111)

X,Y = meshgrid( arange(0,4,.1),arange(0,4,.1) )

xmin,xmax, ymin, ymax=0,3,0,3
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

def f(x,y): return (y+0.2)*(3*x-y**2)/3

def fun(y,x): return f(x,y)

U = 1
V = f(X,Y)

#[mlab.rk4(f, xy, [0, dt])[-1] for xy in pts]

U,V = U/sqrt(U**2+V**2),V/sqrt(U**2+V**2)

plt.axes().set_aspect('equal', 'datalim')

plt.quiver(X,Y,U,V, color='#02ff02', headwidth=0, scale=30)
l,r,b,t = axis()
dx, dy = r-l, t-b
axis([l-0.05*dx, r+0.05*dx, b-0.05*dy, t+0.05*dy])

ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.savefig("smerove_pole.png",bbox_inches="tight", pad_inches=.15)
plt.savefig("smerove_pole.svg",bbox_inches="tight", pad_inches=.15)

# Initial condition

for y0 in [2,3,1.2,.5]:

# Times at which the solution is to be computed.
    t = np.linspace(0, 4, 50)

# Solve the equation.
    y = odeint(fun, y0, t)

# Plot the solution.  `odeint` is generally used to solve a system
# of equations, so it returns an array with shape (len(t), len(y0)).
# In this case, len(y0) is 1, so y[:,0] gives us the solution.
    plt.plot(t, y[:,0])

X,Y = meshgrid( arange(0,4,.1),arange(0,4,.1) )

Z=f(X,Y)
CS = plt.contour(X, Y, Z, 50, linewidths=0.5)



plt.savefig("smerove_pole_2.png",bbox_inches="tight", pad_inches=.15)
plt.savefig("smerove_pole_2.svg",bbox_inches="tight", pad_inches=.15)

