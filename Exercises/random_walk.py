from random import choice


class RandomWalk:
    '''A class to generate random walk data.'''

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Start at 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Calculate all the points in the walk.'''
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self) -> int:
        '''Get the step direction and distance for each step.
           Return an integer for the step size
        '''
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        return direction * distance
