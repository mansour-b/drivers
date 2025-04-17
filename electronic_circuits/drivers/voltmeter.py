import numpy as np

from electronic_circuits.components import Component


class Voltmeter:
    def __init__(self, component: Component):
        self.component = component

    def measure(self) -> float:
        voltage = self.component.get_voltage()
        noise = 0.05 * voltage * (np.random.rand() * 2 - 1)
        return voltage + noise
