from pyfirmata import Arduino, util
import time

# Verbind met de Arduino
board = Arduino('/dev/ttyACM0')

# Stel de pinmodus in
analog_pin = board.get_pin('a:0:i')  # lichtsensor aangesloten op analoge pin 0
led_pin = board.get_pin('d:13:o')    # LED aangesloten op digitale pin 13

# Start de iterator thread om input van analoge pin te lezen
it = util.Iterator(board)
it.start()
analog_pin.enable_reporting()

# Drempelwaarde voor lichtintensiteit
threshold = 0.5

while True:
    light_level = analog_pin.read()  # Lees de lichtsensor
    if light_level is not None:
        if light_level < threshold:
            led_pin.write(1)  # Zet LED aan
        else:
            led_pin.write(0)  # Zet LED uit

    time.sleep(2)  # Wacht voor 2 seconden

    # Hier wordt de sensor niet uitgelezen en wordt er niets gedaan gedurende de delay