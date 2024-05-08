from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')
analog_pin = board.get_pin('a:0:i')
led_pin = board.get_pin('d:13:o')

it = util.Iterator(board)
it.start()
analog_pin.enable_reporting()

threshold = 0.5

while True:
    light_level = analog_pin.read()
    if light_level is not None:
        if light_level < threshold:
            led_pin.write(1)
        else:
            led_pin.write(0)
    time.sleep(2)