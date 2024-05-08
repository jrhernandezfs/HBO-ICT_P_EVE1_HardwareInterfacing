from pyfirmata import Arduino, util
import time

# Verbind met de Arduino
board = Arduino('/dev/ttyACM0')
led_pin = board.get_pin('d:13:o')

while True:
    led_pin.write(1)
    time.sleep(2)  # Blokkerend
    led_pin.write(0)
    time.sleep(2)  # Blokkerend