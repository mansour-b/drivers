import numpy as np

from electronic_circuits.components import Component


class Ammeter:
    def __init__(self, component: Component):
        self.component = component

    def measure(self) -> float:
        current = self.component.get_current()
        noise = 0.05 * current * (np.random.rand() * 2 - 1)
        return current + noise
