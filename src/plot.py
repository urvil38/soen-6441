import numpy as np
import matplotlib.pyplot as plt
from .main import cos

TERM=11
fn=cos
fnn=np.cos
angles = np.arange(-2*np.pi,2*np.pi,0.1)
p_fn = fnn(angles)

fig, ax = plt.subplots()
ax.plot(angles,p_fn)

# add lines for between 1 and 6 terms in the Taylor Series
for i in range(1,TERM+1):
    t_fn = [fn(angle,i) for angle in angles]
    ax.plot(angles,t_fn,linestyle='dotted')

ax.set_ylim([-7,4])

# set up legend
legend_lst = ['cos() function']
for i in range(1,TERM+1):
    legend_lst.append(f'{i} terms')
ax.legend(legend_lst, loc='best')
plt.show()
