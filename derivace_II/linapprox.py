import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
# import my_shared_data_folder.modely_dmp as m
# from scipy import optimize
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset



x = np.linspace(-2,5,500)
fig, ax = plt.subplots()
ax.plot(x,np.sin(x))
ax.plot(x,x)

axins = zoomed_inset_axes(ax, zoom=3, loc='lower right')
eps=0.6
axins.plot(x,np.sin(x))
axins.plot(x,x)
axins.set(xlabel=None, ylabel=None, xlim=(-eps,eps), ylim=(-eps,eps), xticklabels=[], yticklabels=[])

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

mark_inset(ax, axins, loc1=1, loc2=3, ec=".5")
axins.set_facecolor("yellow")
ax.legend(["Funkce sinus, $y=\sin(x)$","Lineární aproximace v poèátku, $y=x$"], loc="upper left")
ax.set(title="Srovnání grafu funkce a její lineární aproximace", ylim=(-4,3))
plt.savefig("linapprox.svg")
