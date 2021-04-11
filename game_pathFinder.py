#!/usr/bin/env python
import numpy as np
import copy
    
def dijkstra(x, y, xb, yb, map, final=[]):
    array = np.array(map, dtype=object)
    FF = [[x+1, y],[x-1, y],[x, y+1],[x, y-1]]
    for i in FF:
        if i == '■':
            pass
        else:
            Fi = copy.deepcopy(final)
            if i[0] == xb and i[1] == yb:
                return final
            elif i[0] == x and i[1] == y:
                pass
            else:
                Fi.append(i)
                return dijkstra(i[0], i[0], xb, yb, array, final)
