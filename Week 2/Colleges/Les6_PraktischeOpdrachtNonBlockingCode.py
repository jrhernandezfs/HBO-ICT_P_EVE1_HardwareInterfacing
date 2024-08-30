from pyfirmata import Arduino, util
import time

# Verbind met de Arduino
board = Arduino('COM3')

# Stel de pinmodus in
analog_pin = board.get_pin('a:0:i')  # lichtsensor aangesloten op analoge pin 0
led_pin = board.get_pin('d:13:o')    # LED aangesloten op digitale pin 13

# Start de iterator thread om input van analoge pin te lezen
it = util.Iterator(board)
it.start()
analog_pin.enable_reporting()

# Drempelwaarde voor lichtintensiteit
threshold = 0.5

last_time = time.time()
interval = 2

while True:
    current_time = time.time()
    if current_time - last_time > interval:
        light_level = analog_pin.read()  # Update en lees de lichtsensor alleen als het interval voorbij is
        if light_level is not None:
            if light_level < threshold:
                led_pin.write(1)
            else:
                led_pin.write(0)
        last_time = current_time  # Reset de timer

    # De rest van de code kan nog steeds uitgevoerd worden zonder onderbreking
