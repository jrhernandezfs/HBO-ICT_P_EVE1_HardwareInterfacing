from pyfirmata import Arduino, util
import time

board = Arduino('COM3') # Vervang 'COM3' door je Arduino-poort
led_pin = board.get_pin('d:13:o') # d: digitale pin, 13: pin nummer, o: output

while True:
    led_pin.write(1) # LED aan
    time.sleep(1000)
    led_pin.write(0) # LED uit
    time.sleep(1000)