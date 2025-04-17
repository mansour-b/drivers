import numpy as np


class Component:
    def __init__(self):
        self.voltage = 0.0

    def set_voltage(self, applied_voltage: float) -> None:
        self.voltage = applied_voltage

    def get_current(self) -> float:
        raise NotImplementedError

    def get_voltage(self) -> float:
        return self.voltage


class Resistor(Component):
    def __init__(self, resistance: float = 1e3):
        self.resistance = resistance

    def get_current(self) -> float:
        return self.voltage / self.resistance


class Diode(Component):
    e_charge: float = 1.6e-19
    boltzmann_constant: float = 1.38e-23

    def __init__(
        self,
        saturation_current: float = 1e-12,
        ideality_factor: float = 1.0,
        temperature: float = 300.0,
    ):
        self.saturation_current = saturation_current
        self.ideality_factor = ideality_factor
        self.temperature = temperature

    def get_current(self) -> float:
        return self.saturation_current * (
            np.exp(
                self.e_charge
                * self.voltage
                / (self.boltzmann_constant * self.temperature)
            )
            - 1
        )
