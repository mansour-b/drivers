from electronic_circuits.circuits import MeasuringCircuit


class TemperatureControlledChamber:
    def __init__(self, circuit: MeasuringCircuit):
        self.circuit = circuit

    def set_temperature(self, temperature: float) -> None:
        for component in self.circuit.components:
            component.set_temperature(temperature)
