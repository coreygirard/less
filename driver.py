import numpy as np
import matplotlib.pyplot as plt
import less


np.random.seed(42)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y2 = y + 0.1 * np.random.normal(size=x.shape)


chart = less.Chart()

# set default and highlight settings
# TODO: change to chart.plot.set_background()
chart.plot_set_background(linestyle='--',color='#BBBBBB')
#chart.scatter_set_background(c='grey',s=3)
#chart.scatter_set_highlight(c='r',s=9)

exit()

# TODO: change to chart.spines.set_visible()
chart.set_visible_spines(['left'])
chart.set_ticks(left=[-1,0,1])
chart.set_ticks(bottom_loc=np.array([0,1,2])*np.pi,
                bottom_label=['{0}$\pi$'.format(i) for i in [0,1,2]])

# split data into highlight and background
mask = np.abs(y-y2) > 0.15

# plot / scatterplot data
chart.plot(x, y)
chart.scatter(x[mask], y2[mask], type='highlight')
chart.scatter(x[mask == False], y2[mask == False], type='background')


chart.scatter(x,y2)
chart.plot(x, y)


chart.render()

'''
mask = np.abs(y-y2) > 0.15
ax.plot(x, y, '--', color='#BBBBBB')

ax.set_xlim((0-0.1, 2*np.pi+0.1))
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
ax.spines['bottom'].set_bounds(0,2*np.pi)
ax.xaxis.set_ticks_position('bottom')

ax.set_ylim((-1.25, 1.25))
ax.set_yticks([-1, 0, 1])
ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_bounds(-1, 1)

ax.spines['left'].set_color('#999999')
ax.spines['right'].set_color('#999999')
ax.tick_params(color='#999999')
ax.yaxis.set_ticks_position('both')

ax.tick_params(labeltop=False, labelright=True)

plt.show()
'''





'''

fig, ax = plt.subplots()

mask = np.abs(y-y2) > 0.15
ax.scatter(x[mask], y2[mask], c='r', s=9)
ax.scatter(x[mask == False], y2[mask == False], c='grey', s=3)

#ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_xlim((0-0.1, 2*np.pi+0.1))
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticklabels(['0', '$\pi$', '2$\pi$'])
ax.spines['bottom'].set_bounds(0,2*np.pi)
ax.xaxis.set_ticks_position('bottom')


ax.set_ylim((-1.25, 1.25))
ax.set_yticks([-1, 0, 1])
ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_bounds(-1, 1)

ax.spines['left'].set_color('#999999')
ax.spines['right'].set_color('#999999')
ax.tick_params(color='#999999')
ax.yaxis.set_ticks_position('both')

ax.tick_params(labeltop=False, labelright=True)

plt.show()
'''
