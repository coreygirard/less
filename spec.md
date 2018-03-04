
## Chart properties

Create chart

```python
chart = less.Chart(width, height)
```

Set spines visible/invisible

```python
chart.spine.left.visible(True)

            [left|right|top|bottom]         [True|False]
chart.spine.                       .visible(            )
```

Set major ticks

```python
chart.spine.bottom.ticks.major([0, np.pi, 2*np.pi],
                               labels=['0', '$\pi$', '2$\pi$'])

                             [list or array of ints/floats]         [list of strings]
chart.spine.left.ticks.major(                              , labels=                 )

                             [list or array of ints/floats]
chart.spine.left.ticks.major(                              )

```

Set minor ticks

```python
chart.spine.bottom.ticks.minor([0, np.pi, 2*np.pi],
                               labels=['0', '$\pi$', '2$\pi$'])
```

Set X limits

```python
chart.xlim(-0.1, 2.1)

           [int or float]  [int or float]
chart.xlim(              ,               )

               [int or float]      [int or float]
chart.ylim(min=              , max=              )

               [int or float]
chart.ylim(min=              )

               [int or float]
chart.ylim(max=              )
```

Set Y limits
```python
chart.ylim(-1.25,1.25)

           [int or float]  [int or float]
chart.ylim(              ,               )

               [int or float]      [int or float]
chart.ylim(min=              , max=              )

               [int or float]
chart.ylim(min=              )

               [int or float]
chart.ylim(max=              )
```

Set title
```python
chart.title('Effects of damping')

            [string]
chart.title(        )
```

Set label
```python
chart.spine.bottom.label('time (s)')

            [left|right|top|bottom]       [string]
chart.spine.                       .label(        )
```

Display chart
```python
chart.render()
```


## Drawing

```
chart.plot()
- name
- x
- y
- style
- alpha, color, etc

```
