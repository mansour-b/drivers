from electronic_circuits.components import Component


class DCVoltageGenerator:
    def __init__(self, component: Component):
        self.component = component

    def set_voltage(self, value: float) -> None:
        self.component.set_voltage(value)
