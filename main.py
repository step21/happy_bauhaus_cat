import network
import time

def connect():
    wlan = network.WLAN(network.STA_IF)
    ssid = "Florians iPhone"
    password = "ichhassemeinleben"
    while not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(ssid, password)

        while wlan.isconnected() == False:
            pass

        print("Connection successful")
        print(wlan.ifconfig())

connect()

from morse import *
from query import *
#msg = "happy birthday"

mq = molochClient().get()
cq = kittyClient().get()

msg = str(mq).strip('{}:,')
ckmsg = str(cq)
print(msg)
print(ckmsg)

m = Morselib()
while True:
    m = Morselib(unicorn=False)
    m.sendString(msg)
    m = Morselib()
    m.sendString(ckmsg)
