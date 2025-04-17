from electronic_circuits.circuits import MeasuringCircuit


class TemperatureControlledChamber:
    def __init__(self, content: MeasuringCircuit):
        self.content = content

    def set_temperature(self, temperature: float) -> None:
        for component in self.content.components:
            component.set_temperature(temperature)
