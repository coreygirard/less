x, y
fmt
data

scalex, scaley : bool, optional, default: True

These parameters determined if the view limits are adapted to the data limits. The values are passed on to autoscale_view.

**kwargs : Line2D properties, optional

kwargs are used to specify properties like a line label (for auto legends), linewidth, antialiasing, marker face color. Example:

>>> plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
>>> plot([1,2,3], [1,4,9], 'rs',  label='line 2')
If you make multiple lines with one plot command, the kwargs apply to all those lines.

Here is a list of available Line2D properties:

Property	Description
agg_filter	a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
alpha	float (0.0 transparent through 1.0 opaque)
animated	bool
antialiased or aa	bool
clip_box	a Bbox instance
clip_on	bool
clip_path	[(Path, Transform) | Patch | None]
color or c	any matplotlib color
contains	a callable function
dash_capstyle	[‘butt’ | ‘round’ | ‘projecting’]
dash_joinstyle	[‘miter’ | ‘round’ | ‘bevel’]
dashes	sequence of on/off ink in points
drawstyle	[‘default’ | ‘steps’ | ‘steps-pre’ | ‘steps-mid’ | ‘steps-post’]
figure	a Figure instance
fillstyle	[‘full’ | ‘left’ | ‘right’ | ‘bottom’ | ‘top’ | ‘none’]
gid	an id string
label	object
linestyle or ls	[‘solid’ | ‘dashed’, ‘dashdot’, ‘dotted’ | (offset, on-off-dash-seq) | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
linewidth or lw	float value in points
marker	A valid marker style
markeredgecolor or mec	any matplotlib color
markeredgewidth or mew	float value in points
markerfacecolor or mfc	any matplotlib color
markerfacecoloralt or mfcalt	any matplotlib color
markersize or ms	float
markevery	[None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
path_effects	AbstractPathEffect
picker	float distance in points or callable pick function fn(artist, event)
pickradius	float distance in points
rasterized	bool or None
sketch_params
snap
solid_capstyle
solid_joinstyle
transform
url
visible
xdata
ydata
zorder
