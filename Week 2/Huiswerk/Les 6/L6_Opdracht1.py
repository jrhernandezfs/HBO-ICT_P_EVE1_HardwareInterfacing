from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')
analog_pin = board.get_pin('a:0:i')
led_pin = board.get_pin('d:13:o')

it = util.Iterator(board)
it.start()
analog_pin.enable_reporting()

threshold = 0.5
last_time = time.time()
interval = 2  # Check de sensor elke 2 seconden

while True:
    current_time = time.time()
    if current_time - last_time >= interval:
        light_level = analog_pin.read()
        if light_level is not None:
            if light_level < threshold:
                led_pin.write(1)  # LED aan
            else:
                led_pin.write(0)  # LED uit
        last_time = current_time  # Reset de timer