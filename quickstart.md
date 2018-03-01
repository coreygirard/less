# Quickstart

**Import _less_**

```python
import less
```

**Creating the chart**

```python
width = 16
height = 9
chart = less.Chart(width, height)
```

**Plot a line**

```python
chart.plot(x, y)
```

**Showing axes**
```python
chart.spine.left.visible(True)
```
