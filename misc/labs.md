```python
chart = less.Chart()
chart.scatter(x=0, y=2, label='point')

x, y1 = chart['point'].coords()
y2 = chart.ymin
chart.plot((x, x), (y1, y2))

x1, y = chart['point'].coords()
x2 = chart.xmin
chart.plot((x1, x2), (y, y), style='--')

chart['point'].draw.to_bottom()
chart['point'].draw.to_left(style='--')

x, y = chart['point'].coords()
```
