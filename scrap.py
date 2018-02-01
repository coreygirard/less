
# labelling
ax.xlabel()
ax.ylabel()
ax.title()

# ticks
ax.tick_params(axis=u'both', which=u'both',length=0)
ax.set_yticks() # minor=True
ax.set_yticklabels()
ax.tick_params(labeltop=False, labelright=True)

plt.tick_params(axis='both',
                which='both',
                bottom='on',
                top='off',
                labelbottom='on',
                left='off',
                right='off',
                labelleft='on',
                color=,
                length=)

plt.xticks([1970,peak_cs_year,2011], fontsize=14)
plt.yticks([50,100],color='#999999',fontsize=14)

ax.tick_params(color='#999999')
ax.xaxis.tick_top()
ax.yaxis.tick_right()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('both')







ax.spines['left'].set_bounds(0,1)
ax.spines['left'].set_visible(False)
ax.spines['left'].set_color('#999999')



plt.show()
plt.show(ax)

ax.plot(x,
        y,
        lw,
        linestyle,
        color,
        xorder,
        alpha)

ax.hist()



ax.set_xlim() # xmin=-1, xmax=1

ax.text(x,
        y,
        text,
        horizontalalignment/ha,
        verticalalignment/va,
        color,
        fontsize,
        alpha,
        rotation,


ax = plt.gca()




fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plt.subplot(2, 1, 1)

fig = plt.figure(figsize=(6,2))
ax = plt.gca()



--------------------------------------------------
