import numpy as np


class Ammeter:
    def __init__(self):
        self.currents = np.arange(-5, 6) / 1e3
        self.index = 0

    def measure(self) -> float:
        res = self.currents[self.index]
        self.index += 1
        return res
