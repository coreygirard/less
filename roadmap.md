# Roadmap

**Docs** <br>
Look into using Slate / Read The Docs?
- Specifications [Markdown]
  - list of all functions, with arguments, etc
- Quickstarts [Markdown with embedded images]
  - Self-contained examples/tutorials for common things
- Gallery [Markdown with embedded images]
  - Eyecandy
  - Another Markdown file that includes related code for chart, linked to from each Gallery image
- "_**less**_ for Matplotlib users"
  - List of function args, and correspondence to Matplotlib args

**Background section shading**
- Specify area and color
- If no x bounds specified, goes to axes limits
- Likewise for y

```python
chart.background(xlim=(2, 5), ylim=(-1, 1), color='grey-100')
chart.background(xlim=(2, 5), color='#ddd')
chart.background(ylim=(-1, 1), color='#eeeeee')
chart.background(xmin=2)
chart.background(xlim=(2, 5), ymin=0)
chart.background(color='black')
```

**Saving images**
  - Support different formats
  - Same appearance printing to screen or saving to file
  - Can specify only width or height, and aspect ratio will be preserved, or specify both
  - Maybe can set chart size in pixels at init?

**New Charts**
- Vertical+horizontal bar
- Vertical+horizontal stacked bar
- Waterfall
  - Try horizontal with thin bars? Labels for data points or deltas
- Square area
- Slopegraph
- Heatmap?
- Table?
- Sparklines
- Histograms
- Cake chart (rectangular version of pie chart)
  - No spines, just names and percentages
  - Stacked vertically for easier labeling

**Theme system**
- Load themes by name
- Save themes by name
- Modify current theme
- Export theme to JSON
- Import theme from JSON (optional arg to set theme name)
- Transform function call kwargs

**Refactor tick/label system**
- `handle_axes.py : Axes() : handle_spine_ticks_major()`
- Streamline spaghetti code
- Preserve functionality for optional labels, bar charts, etc
- Add ability to control tick/label size
- Implement same functionality for minor ticks

**Color system**
- Load colors from JSON
- Save new colors
- Export color JSON to arbitrary file
- Import colors from arbitrary file
- Modifies colors in function kwargs

**Advanced lines**
- Specify multiple colors for a single line
  - List of colors
  - Function that is applied to line points and returns a color
- Make line sections transparent

**Dependencies and pip [moderate]**
- Deploy *telescope* and *foldr* to PyPI

**Scaling system [moderate]**
- Default settings for Jupyter and for presentations
- Perhaps a linear scale that you can choose
- Auto-scale things like text within bars of charts

**Large pretty text [moderate]**
- Engine for creating large text graphics
- Some typesetting geometry required

**Figsize system / subplot system [moderate]**
- Easily set chart size on init
- Easily set chart size after init
- Clean syntax for specifying subplots
- Auto-linking of subplot axes

**Post-processing system [difficult]**
- Support modifying attributes of chart elements after the fact
- Support creating new chart elements based on existing ones
  - Adding labels to existing lines, with default color matching the line
  - Dropping vertical lines from existing points
  - Adding labels to the middle of lines, and erasing that section of line
