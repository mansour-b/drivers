import numpy as np


class Component:
    def get_current(self, applied_voltage: float) -> float:
        raise NotImplementedError


class Resistance(Component):
    def __init__(self, value: float = 1e3):
        self.value = value

    def get_current(self, applied_voltage: float) -> float:
        return applied_voltage / self.resistance


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
        self.ideality_factor = (ideality_factor,)
        self.temperature = temperature

    def get_current(self, applied_voltage: float) -> float:
        return self.saturation_current * (
            np.exp(
                self.e_charge
                * applied_voltage
                / (self.boltzmann_constant * self.temperature)
            )
            - 1
        )
