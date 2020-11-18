import random


class Mate:
    """A basic class for experiments with queues"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "({}, {})".format(self.name, self.value)

    def __lt__(self, other):
        return self.value < other.value

