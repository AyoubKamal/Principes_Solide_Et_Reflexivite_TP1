from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        return "LightBulb: turned on"

    def turn_off(self):
        return "LightBulb: turned off"

class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        return self.device.turn_on()

# Client code
bulb = LightBulb()
switch = Switch(bulb)
print(switch.operate())  # Output: LightBulb: turned on
