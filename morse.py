import time
from machine import Pin
from led import RGBLED

delay = 500


class Morselib:
    def __init__(self, unicorn=True):
        # self.pin = pin
        # self.p = Pin(self.pin, Pin.OUT)
        self.green = 0
        self.blue = 0
        self.red = 0
        self.rgbled = RGBLED()
        self.unicorn = unicorn

    def dot(self):  # , red, green, blue):
        print("dot")
        if self.unicorn:
            self.rgbled.set_unicorn()
            time.sleep_ms(delay)
            self.rgbled.unset()
            time.sleep_ms(delay)
        else:
            self.rgbled.set_rand()  # red, green, blue)
            time.sleep_ms(delay)
            self.rgbled.unset()  # red, green, blue)
            time.sleep_ms(delay)

    def dash(self):  # , red, green, blue):
        print("dash")
        if self.unicorn:
            self.rgbled.set_unicorn()
            time.sleep_ms(3 * delay)
            self.rgbled.unset()
            time.sleep_ms(delay)
        else:
            self.rgbled.set_rand()  # red, green, blue)
            time.sleep_ms(3 * delay)
            self.rgbled.unset()  # red, green, blue)
            time.sleep_ms(delay)

    def sendString(self, msg):
        if msg == None:
            raise Error
        else:
            ml = len(msg)
            print("Message length %s" % ml)
            for i in msg:
                if i == "a":
                    self.a()
                elif i == "b":
                    self.b()
                elif i == "c":
                    self.c()
                elif i == "d":
                    self.d()
                elif i == "e":
                    self.e()
                elif i == "f":
                    self.f()
                elif i == "g":
                    self.g()
                elif i == "h":
                    self.h()
                elif i == "i":
                    self.i()
                elif i == "j":
                    self.j()
                elif i == "k":
                    self.k()
                elif i == "l":
                    self.l()
                elif i == "m":
                    self.m()
                elif i == "n":
                    self.n()
                elif i == "o":
                    self.o()
                elif i == "p":
                    self.p()
                elif i == "q":
                    self.q()
                elif i == "r":
                    self.r()
                elif i == "s":
                    self.s()
                elif i == "t":
                    self.t()
                elif i == "u":
                    self.u()
                elif i == "v":
                    self.v()
                elif i == "w":
                    self.w()
                elif i == "x":
                    self.x()
                elif i == "y":
                    self.y()
                elif i == "0":
                    self.zero()
                elif i == "1":
                    self.one()
                elif i == "2":
                    self.two()
                elif i == "3":
                    self.three()
                elif i == "4":
                    self.four()
                elif i == "5":
                    self.five()
                elif i == "6":
                    self.six()
                elif i == "7":
                    self.seven()
                elif i == "8":
                    self.eight()
                elif i == "9":
                    self.nine()
                elif i == ".":
                    self.fullstop()
                elif i == " ":
                    self.wordpause()
                    print("Wortende\n")
                else:
                    print('undefined state')

    def a(self):
        self.dot()
        self.dash()

    def b(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot()

    def c(self):
        self.dash()
        self.dot()
        self.dash()
        self.dot()

    def d(self):
        self.dash()
        self.dot()
        self.dot()

    def e(self):
        self.dot()

    def f(self):
        self.dot()
        self.dot()
        self.dash()
        self.dot()

    def g(self):
        self.dash()
        self.dash()
        self.dot()

    def h(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()

    def i(self):
        self.dot()
        self.dot()

    def j(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash()

    def k(self):
        self.dash()
        self.dot()
        self.dash()

    def l(self):
        self.dot()
        self.dash()
        self.dot()
        self.dot()

    def m(self):
        self.dash()
        self.dash()

    def n(self):
        self.dash()
        self.dot()

    def o(self):
        self.dash()
        self.dash()
        self.dash()  # The letter O consists of three dash();es

    def p(self):
        self.dot()
        self.dash()
        self.dash()
        self.dot()

    def q(self):
        self.dash()
        self.dash()
        self.dot()
        self.dash()

    def r(self):
        self.dot()
        self.dash()
        self.dot()

    def s(self):
        self.dot()
        self.dot()
        self.dot()  # The letter S consists of three dot();s

    def t(self):
        self.dash()

    def u(self):
        self.dot()
        self.dot()
        self.dash()

    def v(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()

    def w(self):
        self.dot()
        self.dash()
        self.dash()

    def x(self):
        self.dash()
        self.dot()
        self.dot()
        self.dash()

    def y(self):
        self.dash()
        self.dot()
        self.dash()
        self.dash()

    def z(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()

    def one(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash()
        self.dash()

    def two(self):
        self.dot()
        self.dot()
        self.dash()
        self.dash()
        self.dash()

    def three(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        self.dash()

    def four(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dash()

    def five(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dot()

    def six(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot()
        self.dot()

    def seven(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()
        self.dot()

    def eight(self):
        self.dash()
        self.dash()
        self.dash()
        self.dot()
        self.dot()

    def nine(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dot()

    def zero(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dash()

    def fullstop(self):
        self.dot()
        self.dash()
        self.dot()
        self.dash()
        self.dot()
        self.dash()

    def wordpause(self):
        print("Wortpause")
        time.sleep_ms(7 * delay)
