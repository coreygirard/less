import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("/Users/coreygirard/Documents/GitHub/telescope")
import telescope


def get_via_x(x, y, xi):
    if not isinstance(xi, list):
        xi = [xi]

    temp = []
    for a, b, c, d in zip(x, y, x[1:], y[1:]):
        if len(xi) == 0:
            break

        if len(xi) > 0 and a == xi[0]:
            temp.append(((a, b), (a, b), xi.pop(0)))

        if len(xi) > 0 and ((a < xi[0]) != (c < xi[0])):
            if a < c:
                temp.append(((a, b), (c, d), xi.pop(0)))
                continue
            elif c < a:
                temp.append(((c, d), (a, b), xi.pop(0)))
                continue

    print(temp)

    results = []
    for (a, b), (c, d), e in temp:
        if a == e:
            results.append((e, b))
            continue

        slope = (d-b)/(c-a)
        new_y = b + slope*(e-a)
        results.append((e, new_y))

    return results

def get_via_t(x, y, t):
    assert len(x) == len(y)
    assert t >= 0 and t <= 1

    t *= len(x) - 1
    if int(t) == t:
        t = int(t)
        return x[t], y[t]
    # else:
    below, above = int(t), int(t) + 1
    w_below, w_above = t-below, above-t
    return (x[below]*w_below + x[above]*w_above,
            y[below]*w_below + y[above]*w_above)



#x = [1, 2, 3, -1]
#y = [3, 0, 5, -2]
#print(get_via_x(x, y, [1, 1.5, 0.5]))

x = [1, 2, 3]
y = [0, 5, 2.5]
print(get_via_x(x, y, [1.5, 2.0, 2.5]))
