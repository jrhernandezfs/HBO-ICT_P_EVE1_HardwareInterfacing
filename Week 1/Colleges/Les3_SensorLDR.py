from pyfirmata import Arduino, util
import time

board = Arduino('COM3') # Vervang met correcte poort
it = util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:
    light_value = analog_input.read()
    print(f"LDR_value = {light_value}")
    time.sleep(1000)