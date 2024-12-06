from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

initial_state = np.array([
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

n = len(initial_state)
A = np.zeros((n, n))
np.fill_diagonal(A, 1)
A[np.arange(1, n) % n, np.arange(n-1)] = -1

k = 255
u = initial_state.copy()
evolution = [u.copy()]  

for _ in range(k):
    u = u - 0.5 * A @ u
    evolution.append(u.copy())

evolution = np.array(evolution)

fig, ax = plt.subplots(figsize=(12, 6))
line, = ax.plot([], [], lw=2)

ax.set_xlim(1, n)
ax.set_ylim(np.min(evolution), np.max(evolution))
ax.set_xlabel('x')
ax.set_ylabel('u(x)')
ax.set_title('Changing u(x) over Time')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(np.arange(1, n + 1), evolution[frame])
    ax.set_title(f'Changing u(x) at time step {frame}')
    return line,

anim = FuncAnimation(fig, update, frames=range(k + 1), init_func=init, blit=True)
anim.save('1.gif', writer='pillow', fps=60)
plt.show()
