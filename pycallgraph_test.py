from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput



config = Config()
config.trace_filter = GlobbingFilter(exclude=[
    '*_find_and_load_unlocked',
    '*_load_unlocked',
    '*_handle_fromlist',
    '*ModuleSpec*'
])

import numpy as np
import matplotlib.pyplot as plt
import less

np.random.seed(42)

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

y2 = y + 0.1 * np.random.normal(size=x.shape)
mask = np.abs(y-y2) > 0.18

# tweak one point to be better within bounds
i = [i for i,e in enumerate(mask) if e][-1]
y2[i] += 2*(y[i]-y2[i])

typical_x,typical_y = x[mask == False],y2[mask == False]
outlier_x,outlier_y = x[mask],y2[mask]


with PyCallGraph(output=GraphvizOutput(), config=config):
    # create chart
    chart = less.Chart(9,6) # args set size

    # draw data elements
    chart.plot(x=x, y=y) # defaults to dashed line
    chart.scatter(x=typical_x, y=typical_y, style='background') # grey
    chart.scatter(x=outlier_x, y=outlier_y, style='highlight') # color

    # creating and styling left axis
    chart.spine.left.visible(True)
    chart.spine.left.ticks.major([-1,0,1])
    chart.spine.left.ticks.minor(outlier_y)

    # creating and styling right axis
    chart.spine.right.visible(True)
    chart.spine.right.ticks.major([-1,0,1])
    chart.spine.right.ticks.minor(outlier_y)

    # creating ticks on bottom axis
    chart.spine.bottom.ticks.major([0, np.pi, 2*np.pi],
                                   labels=['0', '$\pi$', '2$\pi$'])
    chart.spine.bottom.ticks.minor(outlier_x)

    # setting extent of chart area
    chart.xlim(-0.1, 2*np.pi+0.1)
    chart.ylim(-1.25,1.25)

    # similar to plt.show()
    #chart.render()
