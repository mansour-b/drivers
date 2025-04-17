import numpy as np


class Ammeter:
    def __init__(self):
        self.currents = np.arange(-5, 6) / 1e3
        self.index = 0

        min_current = self.currents.min()
        max_current = self.currents.max()

        noise = (
            0.1
            * (max_current - min_current)
            * np.random.rand(len(self.currents))
            + min_current
        )
        self.currents += noise

    def measure(self) -> float:
        res = self.currents[self.index]
        self.index += 1
        return res
