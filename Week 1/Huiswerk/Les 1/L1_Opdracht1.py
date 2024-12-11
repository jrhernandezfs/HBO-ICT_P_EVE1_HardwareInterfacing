import pyfirmata2
import time

# Maak verbinding met de Arduino
PORT = pyfirmata2.Arduino.AUTODETECT  # Detecteert automatisch de juiste poort
board = pyfirmata2.Arduino(PORT)  # Vervang 'COM9' door de juiste poort

# Definieer de pin
led_pin = 12  # Pin 12

while True:
    board.digital[led_pin].write(1)  # Zet LED aan
    time.sleep(1)
    board.digital[led_pin].write(0)  # Zet LED uit
    time.sleep(1)