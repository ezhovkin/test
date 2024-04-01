import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.ticker import FuncFormatter

plt.ion()

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.25)
ax.tick_params(axis='both', labelsize=12, labelcolor='blue')


def with_space(x, pos):
    return f"{int(x):,}".replace(',', ' ') + ' руб'

ax.yaxis.set_major_formatter(FuncFormatter(with_space))
fig.canvas.manager.set_window_title('Окно не требующее plt.show()')
ax.set_ylabel('Доход', fontsize=14, color='red')

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) * 10000
line, = ax.plot(x, y)

ax.set_ylim([-11000, 11000])
ax.set_yticks(np.arange(-10000, 10001, 5000))
ax.set_xlim([0, max(x)])

text = ax.text(0.5, 1.05, '«Кто мы, откуда, куда мы идём?»', horizontalalignment='left',
               verticalalignment='center', transform=ax.transAxes, color='red', size=12)

for i in range(200):
    line.set_ydata(np.sin(x + i * np.pi / 50) * 10000)
    text.set_position((0.9 - 0.01 * i, 1.05))
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

# plt.show()
