import numpy as np


class Voltmeter:
    def __init__(self):
        self.voltages = np.arange(-5, 6)
        self.index = 0

    def measure(self) -> float:
        res = self.voltages[self.index]
        self.index += 1
        return res
