```python
# create chart
chart = less.Chart(9, 6)  # these arguments set actual image size

# draw data elements
chart.scatter(typical_x, typical_y, style='background')
chart.scatter(outlier_x, outlier_y, style='highlight')

# styling left axis
chart.spine.left(visible=True,  # controls the line itself, not the ticks
                 ticks_major=[-1, 0, 1],
                 ticks_minor=outlier_y)

# styling right axis
chart.spine.right(visible=True,
                  ticks_major=[-1, 0, 1],
                  ticks_minor=outlier_y)

# creating ticks on bottom axis
chart.spine.bottom(ticks_major=[0, np.pi, 2*np.pi],
                   ticks_major_labels=['0', '$\pi$', '2$\pi$'],
                   ticks_minor=outlier_x)

# setting extent of chart area
chart.limits(x=[-0.1, 2*math.pi+0.1],
             y=[-1.25, 1.25])

# create SVG
chart.render()
```
