from pprint import pprint
import json
import matplotlib.pyplot as plt


with open('colors.json', 'r') as f:
    data = json.load(f)




def convert(h):
    return int(h[1:3],16),int(h[3:5],16),int(h[5:7],16)

with open('colors.json','r') as f:
    data = json.load(f)

def tweak_axes(ax):
    ticks = range(0,256+1,64)

    ax.set_aspect('equal', 'box')
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_yticks(ticks)
    ax.set_xticks(ticks)
    ax.set_xlim(0-10, 255+10)
    ax.set_ylim(0-10, 255+10)


def plot_data(data, ax1, ax2, ax3, linecolor, alpha):

    tweak_axes(ax1)
    tweak_axes(ax2)
    tweak_axes(ax3)

    red = [i[0] for _,_,i in d]
    green = [i[1] for _,_,i in d]
    blue = [i[2] for _,_,i in d]

    ax1.set_title('Red vs Green')
    ax1.set_xlabel('Red')
    ax1.set_ylabel('Green')
    ax1.plot(red, green, '-', color=linecolor, alpha=alpha, zorder=1)

    ax2.set_title('Green vs Blue')
    ax2.set_xlabel('Green')
    ax2.set_ylabel('Blue')
    ax2.plot(green, blue, '-', color=linecolor, alpha=alpha, zorder=1)

    ax3.set_title('Blue vs Red')
    ax3.set_xlabel('Blue')
    ax3.set_ylabel('Red')
    ax3.plot(blue, red, '-', color=linecolor, alpha=alpha, zorder=1)

    '''
    for k,v,(r,g,b) in d:
        ax1.scatter(r,g,color=v, alpha=1, s=20, zorder=2)
        ax2.scatter(g,b,color=v, alpha=1, s=20, zorder=2)
        ax3.scatter(b,r,color=v, alpha=1, s=20, zorder=2)
    '''


plt.rcParams["figure.figsize"] = [15,5]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

for color in list(data.keys()) + ['red']:
    print(color)

    if type(data[color]) == str:
        continue

    d = sorted([(k, v, convert(v)) for k,v in data[color].items() if len(k) == 3])

    if color == 'red':
        linecolor, alpha = 'orange', 1.0
    else:
        linecolor, alpha = 'k', 0.2

    plot_data(d, ax1, ax2, ax3, linecolor, alpha)

plt.show(fig)
