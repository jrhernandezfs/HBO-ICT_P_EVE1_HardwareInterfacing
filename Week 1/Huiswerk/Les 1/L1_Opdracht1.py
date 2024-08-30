from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('COM9')  # Vervang 'COM9' door de juiste poort

# Definieer de pin
led_pin = board.get_pin('d:12:o')

while True:
        led_pin.write(1)  # Zet LED aan
        time.sleep(1)
        led_pin.write(0)  # Zet LED uit
        time.sleep(1)