from electronic_circuits.components import Component
from electronic_circuits.drivers import Ammeter, DCVoltageGenerator, Voltmeter


class MeasuringCircuit:
    def __init__(self, component: Component):
        self.component = component
        self.generator = DCVoltageGenerator(component)

        self.ammeter = Ammeter(component)
        self.voltmeter = Voltmeter(component)

        self.components = [component]
