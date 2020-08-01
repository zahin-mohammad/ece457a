
import numpy as np


class Particle(object):
    def __init__(self,
                 x_range,
                 y_range,
                 position=None,
                 velocity=None):

        self.position = position
        if self.position is None:
            self.position = np.array([
                np.random.uniform(x_range[0], x_range[1]),
                np.random.uniform(y_range[0], y_range[1]),
            ])

        self.velocity = np.zeros(self.position.shape)
        self.p_best = self.position

    def fly(self,
            global_best,
            velocity_update_fn,
            fitness_fn):

        # Update velocity
        self.velocity = velocity_update_fn(
            self.velocity, self.position, self.p_best, global_best)

        # Update position
        self.position = self.position + self.velocity

        # update personal_best
        self.p_best = min([self.p_best, self.position],
                          key=lambda pos: fitness_fn(pos[0], pos[1]))
