class LightBulb:
    def turn_on(self):
        return "LightBulb: turned on"

    def turn_off(self):
        return "LightBulb: turned off"

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        return self.bulb.turn_on()

# Client code
bulb = LightBulb()
switch = Switch(bulb)
print(switch.operate())  # Output: LightBulb: turned on
