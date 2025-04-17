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

    def set_temperature(self, temperature: float) -> None:
        pass


class Resistor(Component):
    def __init__(self, resistance: float = 1e3):
        self.resistance = resistance

    def get_current(self) -> float:
        return self.voltage / self.resistance


class TemperatureDependentComponent(Component):
    temperature = 300.0

    def set_temperature(self, temperature: float) -> None:
        self.temperature = temperature


class Diode(TemperatureDependentComponent):
    e_charge: float = 1.6e-19
    boltzmann_constant: float = 1.38e-23

    def __init__(
        self, saturation_current: float = 1e-12, ideality_factor: float = 1.0
    ):
        self.saturation_current = saturation_current
        self.ideality_factor = ideality_factor

    def get_current(self) -> float:
        return self.saturation_current * (
            np.exp(
                self.e_charge
                * self.voltage
                / (self.boltzmann_constant * self.temperature)
            )
            - 1
        )


class Thermistor(TemperatureDependentComponent):
    def __init__(
        self,
        r_0: float = 1e3,
        beta: float = 3000.0,
        t_0: float = 300.0,
    ):
        self.r_0 = r_0
        self.beta = beta
        self.t_0 = t_0

    def get_current(self) -> float:
        resistance = self.r_0 * np.exp(
            self.beta * (1 / self.temperature - 1 / self.t_0)
        )
        return self.voltage / resistance
