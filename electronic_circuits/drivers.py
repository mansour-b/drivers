import numpy as np

from electronic_circuits.components import Component


class DCVoltageGenerator:
    def __init__(self, component: Component):
        self.component = component

    def set_voltage(self, value: float) -> None:
        self.component.set_voltage(value)


class Voltmeter:
    def __init__(self, component: Component):
        self.component = component

    def measure(self) -> float:
        voltage = self.component.get_voltage()
        noise = 0.05 * voltage * (np.random.rand() * 2 - 1)
        return voltage + noise


class Ammeter:
    def __init__(self, component: Component):
        self.component = component

    def measure(self) -> float:
        current = self.component.get_current()
        noise = 0.05 * current * (np.random.rand() * 2 - 1)
        return current + noise
