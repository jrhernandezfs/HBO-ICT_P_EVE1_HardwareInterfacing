from pyfirmata2 import Arduino
import time

# Maak verbinding met de Arduino
PORT = Arduino.AUTODETECT  # Detecteert automatisch de juiste poort
board = Arduino(PORT)

print("Arduino gestart")
board.samplingOn(100)  # Stel de bemonsteringsinterval in op 100 ms (standaard is 19 ms)

# Callback-functie voor de knop
def knop_callback(value):
    global knop_gedrukt
    knop_gedrukt = not value  # Keer de knopstatus om (waarde 0 is knop ingedrukt)

# LED-functie
def set_led():
    if knop_gedrukt:
        led_pin.write(1)  # Zet LED aan
    else:
        led_pin.write(0)  # Zet LED uit

# Instellen van de knop- en LED-pinnen
knop_pin = board.get_pin("d:2:i")  # Digitale pin 2 als input
knop_pin.register_callback(knop_callback)  # Registreer de callback voor de knop
knop_pin.enable_reporting()  # Schakel het rapporteren in

led_pin = board.get_pin("d:11:o")  # Digitale pin 6 als output
knop_gedrukt = False  # Beginstatus van de knop

# Hoofdloop
while True:
    set_led()  # Pas LED-status aan op basis van de knopstatus
    time.sleep(0.01)  # Een korte pauze voor stabiliteit