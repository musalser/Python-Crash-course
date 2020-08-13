from random import choice


class RandomWalk():
    """Class to generate random walks"""

    def __init__(self, numpoints=5000):
        self.numpoints = numpoints

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.numpoints:
            x_dir = choice([-1, 1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist

            y_dir = choice([-1, 1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dist

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
