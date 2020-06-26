import matplotlib.pyplot as plot
import numpy as np
from easom import f
from state import get_random_state
from simulated_annealing import perform_annealing_and_print
from cost import cost
from next_neighbor import next_neighbor
from annealing_schedule import make_trigonometric_schedule


fig = plot.figure(figsize=plot.figaspect(0.5))

configs = [
    ('Trigonometric Schedule', 0.001, 0.00001,
     1000, make_trigonometric_schedule(3000)),
]

i = 1
num_plots = len(configs) + 1
for name, initial_temp, final_temp, iter_per_T, schedule in configs:
    print(f'Running {name}')
    ax = fig.add_subplot(1, num_plots, i, projection='3d')

    states, costs = perform_annealing_and_print(
        get_random_state(),
        schedule,
        initial_temp,  # starting temp
        final_temp,
        iter_per_T,
        cost,
        next_neighbor
    )
    i += 1
    ax.plot3D([x1 for x1, _ in states], [x2 for _, x2 in states], costs)

ax = fig.add_subplot(1, num_plots, i, projection='3d')
x = y = np.linspace(-10, 10, 10000)
X, Y = np.meshgrid(x, y)
zs = np.array(f((np.ravel(X), np.ravel(Y))))
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z)


plot.show()
