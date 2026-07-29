from cycler import cycler

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
# mpl.rcParams['lines.linewidth']=2
# mpl.rcParams['lines.linestyle']='--'
# mpl.rcParams['axes.prop_cycle']=cycler(color=['r','g','b','y'])
# mpl.rc('lines',linewidth=4,linestyle='-.')
@mpl.rc_context({'lines.linewidth':3,'lines.linestyle':'--'})
def plotting_function():
    data=np.random.randn(100)
    plt.plot(data)
    
plotting_function()
# with mpl.rc_context({'lines.linewidth':2,'lines.linestyle':':'}):
plt.show()