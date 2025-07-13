import random
import math

class Distribution:
    def __init__(self, dist_type="normal"):
        self.dist_type = dist_type
        self.set_parameters()

    def set_parameters(self):
        if self.dist_type == "normal":
            self.mean = 100
            self.stddev = 20
        elif self.dist_type == "regular":
            self.mean = 100
            self.stddev = 20
        elif self.dist_type == "equal_revenue":
            pass
        else:
            print("error set dist")

    def sample(self):
        if self.dist_type == "normal":
            return random.gauss(self.mean, self.stddev)
        elif self.dist_type == "regular":
            return random.gauss(self.mean, self.stddev)
        elif self.dist_type == "equal_revenue":
            u = random.random()
            return 1.0 / (1.0 - u)
        else:
            print("error dist")