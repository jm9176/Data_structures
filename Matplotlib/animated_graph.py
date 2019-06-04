import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
plt1 = fig.add_subplot(1,1,1)

def animate(i):
    x = np.linspace(0,2,1000)
    y = np.sin(2*np.pi*(x-0.01*i))plt.
    plt1.clear()
    plt1.axis([0, 2, -2, 2])
    plt1.plot(x,y)

x, y = 1, 1
anim = animation.FuncAnimation(fig, animate, interval = 10)

plt.show()
