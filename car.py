from abc import ABC, abstractmethod
from engine.engine import Engine
from engine.battery import Battery


class Car(ABC):
    def __init__(self, last_service_date = None):
        self.last_service_date = last_service_date
        self.engine = None
        self.battery = None

    def needs_service(self):
        pass

    def create_calliope(self):
        self.engine = ()
        self.battery = Battery.SpindlerBattery()

    def create_glissade(self):
        self.engine = Engine.WilloughbyEngine()
        self.battery = Battery.SpindlerBattery()

    def create_palindrome(self):
        self.engine = Engine.SternmanEngine()
        self.battery = Engine.SpindlerBattery()

    def create_rorschach(self):
        self.engine = Engine.WilloughbyEngine()
        self.battery = Battery.NubbinBattery()

    def create_thovex(self):
        self.engine = Engine.CapuletEngine()
        self.battery = Battery.NubbinBattery()

c1 = Car()
c1.create_calliope()

print(c1.engine)
