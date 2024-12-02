from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Intializes attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):
        """A method to get the direction and number of steps. HOWEVER, this assumes X and Y steps are equal.
        A different set-up could be done so that these are differentiated so that arguments could be given to modify
        the range for distance, then differentiated in fill_walk()"""
       # x_direction = choice([1, -1])
       # x_distance = choice([0, 1, 2, 3, 4, 5, 6])
       #x_step = x_direction * x_distance

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance


    def fill_walk(self):
        """Calculate all the points in a walk."""
        # Keep taking steps until the walk reaches the desired length


        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far

            x_step = self.get_step()
            y_step = self.get_step()

            #Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
