# less

The beautiful graphing library

## why?

[Matplotlib](https://matplotlib.org/gallery/index.html) is an amazing library. It enables almost any kind of graphing you could possibly want. Lately, though, I've found myself wanting two things:

- Easy [minimal](https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/) plots without a lot of code required to turn various default ~~chartjunk~~ elements off
- A slightly more intuitive / uniform interface to the various elements. I've only got so much time, and I'd rather not spend it in the docs seeing if I should use `.set_xlim()` or `.set_bounds()`, `.tick_params` or `.set_ticks_position()`.

*less* is my attempt to address both of those personal pain points. Let's look at an example of how things work out of the box, **Matplotlib** vs **_less_**. First, we'll create some data points:

```python
np.random.seed(42)

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

y2 = y + 0.1 * np.random.normal(size=x.shape)
mask = np.abs(y-y2) > 0.18

i = [i for i,e in enumerate(mask) if e][-1]
y2[i] += 2*(y[i]-y2[i])

typical_x,typical_y = x[mask],y2[mask]
outlier_x,outlier_y = x[mask == False],y2[mask == False]
```
Now we'll plot it with **Matplotlib**'s default settings:

```python
plt.figure(figsize=(9,6))

plt.plot(x, y)
plt.scatter(typical_x, typical_y)
plt.scatter(outlier_x, outlier_y)

plt.show()
```

![img](http://i.imgur.com/TeVy7LQ.png)

And plotting it with **_less_**'s default settings:

```python
chart = less.Chart(9,6)

chart.plot(x, y)

chart.scatter(typical_x, typical_y)
chart.scatter(outlier_x, outlier_y)

chart.render()
```

![img](http://i.imgur.com/On5uIHs.png)

Now obviously the second graph isn't very informative as is. No axes, no labels, no color. But the philosophy of **_less_** is that every element in a graph should be there for a specific reason. To that end, its design requires you to add every single element by hand. Let's see a usable graph made with **_less_**:

```python
# create chart
chart = less.Chart(9,6) # args set size

# draw data elements
chart.plot(x, y) # defaults to dashed line
chart.scatter(typical_x, typical_y, style='highlight') # color
chart.scatter(outlier_x, outlier_y, style='background') # grey

# creating and styling left axis
chart.spine.left.visible(True)
chart.spine.left.ticks.major([-1,0,1])
chart.spine.left.ticks.minor(y2[mask])

# creating and styling right axis
chart.spine.right.visible(True)
chart.spine.right.ticks.major([-1,0,1])
chart.spine.right.ticks.minor(y2[mask])

# creating ticks on bottom axis
chart.spine.bottom.ticks.major([0, np.pi, 2*np.pi],
                               labels=['0', '$\pi$', '2$\pi$'])
chart.spine.bottom.ticks.minor(x[mask])

# setting extent of chart area
chart.xlim((-0.1, 2*np.pi+0.1))
chart.ylim((-1.25,1.25))

# similar to plt.show()
chart.render()
```

![img](https://i.imgur.com/vTSDmLh.png)

- We specify some of the points to be highlighted, and **_less_** uses its default color schemes to draw attention to only those points.
- Scatter plot data points are by default drawn smaller than **Matplotlib**'s defaults, for a cleaner style.
- We manually make the left and right axes visible. Everything else stays undrawn by default.
- Setting our tick locations automatically limits the axis to being drawn only between those locations.
- When we're drawing the bottom ticks, we specify an optional `labels` argument.

Every visible element is there as a conscious choice, and I would argue the end result is both more beautiful and more informative as a result.
