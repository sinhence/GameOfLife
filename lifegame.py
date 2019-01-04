"""
The Rules
For a space that is populated:
    Each cell with one or no neighbors dies, as if by solitude.
    Each cell with four or more neighbors dies, as if by overpopulation.
    Each cell with two or three neighbors survives.
For a space that is empty or unpopulated:
    Each cell with three neighbors becomes populated.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_size = 50
y_size = 50

life = np.random.randint(0, 2, [x_size, y_size])
life_state = life.copy()
x_data, y_data = [], []
fig, ax = plt.subplots()
cells, = ax.plot([], [], 'go', markersize=5, animated=False)


def init():
    ax.set_xlim(0, x_size)
    ax.set_ylim(0, y_size)
    return cells,


def update(n):
    plt.title(n)
    x_data.clear()
    y_data.clear()
    for i in range(x_size):
        for j in range(y_size):
            left = x_size - 1 if i - 1 < 0 else i - 1
            right = 0 if i + 1 > x_size - 1 else i + 1
            bottom = y_size - 1 if j - 1 < 0 else j - 1
            top = 0 if j + 1 > y_size - 1 else j + 1
            neighbours = life[left, top] + life[left, j] + life[left, bottom] + life[i, top] + life[i, bottom] + life[
                right, top] + life[right, j] + life[right, bottom]

            if neighbours < 2 or neighbours > 3:
                life_state[i, j] = 0
            elif neighbours == 3:
                life_state[i, j] = 1

            if life[i, j] == 1:
                x_data.append(i)
                y_data.append(j)

    np.copyto(life, life_state)
    cells.set_data(x_data, y_data)
    return cells,


ani = FuncAnimation(fig=fig, func=update, init_func=init, interval=500, blit=False, frames=10000000000000000)

plt.show()
