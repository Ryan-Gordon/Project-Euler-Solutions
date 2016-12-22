"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down.
There are exactly 6 routes to the bottom right corner.

How many such routes are there throught a 20x20 grid?
"""

import time
def route_num(cube_size): # cube_size is the amount of rows and columns
    LatticePaths = [1] * cube_size #LatticePaths
    for i in range(cube_size): # For rows in grid
        for j in range(i): # For column of each row
            LatticePaths[j] = LatticePaths[j] + LatticePaths[j - 1]
        LatticePaths[i] = 2 * LatticePaths[i - 1]
    return LatticePaths[cube_size - 1] # Returns the number of lattice paths


start = time.time()
n = route_num(20) # Do the function and get lattice paths.
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n, elapsed)