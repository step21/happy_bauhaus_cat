import machine
from randint import randint

class RGBLED:
    def __init__(self):
        self.pin_green = 12
        self.pin_red = 4
        self.pin_blue = 14
        self.pin_r = machine.PWM(machine.Pin(self.pin_red))
        self.pin_g = machine.PWM(machine.Pin(self.pin_green))
        self.pin_b = machine.PWM(machine.Pin(self.pin_blue))
        self.set(0, 0, 0)

    def set(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.duty()
    
    def set_unicorn(self,):
        self.r = 100
        self.g = 0
        self.b = 100
        self.duty()

    def set_rand(self):
        self.r = randint(0, 1023)
        self.g = randint(0, 1023)
        self.b = randint(0, 1023)
        self.duty()

    def unset(self):
        self.set(0,0,0)

    def duty(self):
        self.pin_r.duty(self.duty_translate(self.r))
        self.pin_g.duty(self.duty_translate(self.g))
        self.pin_b.duty(self.duty_translate(self.b))

    def duty_translate(self, n):
        """translate values from 0-255 to 0-1023"""
        return int((float(n) / 255) * 1023)
