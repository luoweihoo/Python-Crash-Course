# @File    :   rw_visual.py
# @Time    :   2019/11/02 23:01:18
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as program is active
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, 
                cmap = plt.cm.Blues, edgecolors = 'none', s = 15)

    # Emphasize the first and last points
    ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
    
    plt.show()

    keep_ruuning = input("Make another walk? (y/n): ")
    if keep_ruuning == 'n':
        break