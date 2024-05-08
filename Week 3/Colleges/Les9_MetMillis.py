from pyfirmata import Arduino, util
import time

# Verbind met de Arduino
board = Arduino('/dev/ttyACM0')
led_pin = board.get_pin('d:13:o')

previous_millis = 0
interval = 2000  # Interval in milliseconden

while True:
    current_millis = int(round(time.time() * 1000))
    if current_millis - previous_millis >= interval:
        led_pin.write(not led_pin.read())  # Toggle LED status
        previous_millis = current_millis
