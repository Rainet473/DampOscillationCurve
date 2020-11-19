import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import MovieWriter
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [],  markersize=2, color='blue')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def y_damp(frame):
    t = frame
    y = ((np.exp(-0.6*t))*np.cos(2*np.pi*t))
    return y
t = np.arange(0, 2*np.pi, 0.01)
y = (np.exp(-0.6*t))
plt.plot(t, y, 'r', linestyle="dotted", markersize=12)

y = -(np.exp(-0.6*t))
plt.plot(t, y, 'r', linestyle="dotted", markersize=12)

def update(frame):
    xdata.append(frame)
    ydata.append(y_damp(frame))
    ln.set_data(xdata, ydata)
    return ln,

plt.xlabel("Time --->")
plt.ylabel("Amplitude ---->")
plt.title("DAMPED OSCILLATION")
plt.axhline(color='black')

ani = FuncAnimation(fig, update, frames= np.linspace(0, 2*np.pi, 256),
                    init_func=init, interval = 1)

ani.save('myAnimation.gif', writer='pillow', fps=30)
