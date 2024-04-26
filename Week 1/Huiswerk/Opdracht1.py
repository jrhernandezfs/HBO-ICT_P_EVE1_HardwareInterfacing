from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('/dev/ttyACM0')  # Vervang '/dev/ttyACM0' door de juiste poort

# Definieer de pin
led_pin = board.get_pin('d:13:o')

while True:
        led_pin.write(1)  # Zet LED aan
        time.sleep(1)
        led_pin.write(0)  # Zet LED uit
        time.sleep(1)