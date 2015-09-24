# Imagine a large ball hanging down on the end of a vertical rod. 
# Imagine a truck slides towards it, pushing it up and out of the way.
# If the truck has position a and the rod has rotation b, plot b against a and
# put an 'x' if the two are intersecting, else a '.'. What shape does the intersection
# region have in that state space?

import math
import numpy as np

def doesCircleIntersectPoint(cx,cy,r,px,py):
    return math.hypot(cx-px,cy-py) < r
    
r = 1
for b in np.arange(-2,2,0.1):
    cx = math.sin(b)
    cy = math.cos(b)-1
    for a in np.arange(-2,2,0.1):
        px = a
        py = 0
        if doesCircleIntersectPoint(cx,cy,r,px,py):
            print 'x',
        else:
            print '.',
    print ''