# @File    :   scatter_squares.py
# @Time    :   2019/11/02 14:09:30
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = 'red', s = 10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the ragne for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches = 'tight')