from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('/dev/ttyACM0')  # Vervang '/dev/ttyACM0' door de juiste poort

# Definieer de pins
led_pins = [board.get_pin(f'd:{pin}:o') for pin in (10, 11, 12)]

def blink_leds(pattern):
    """ Laat de LED's knipperen volgens een gegeven patroon. """
    for state, duration in pattern:
        for pin, status in zip(led_pins, state):
            pin.write(status)
        time.sleep(duration)

# Definieer een patroon
# (LED states, duration in seconds)
pattern = [
    ((1, 0, 0), 1),  # Alleen LED op pin 10
    ((0, 1, 0), 1.5),  # Alleen LED op pin 11
    ((0, 0, 1), 2)  # Alleen LED op pin 12
]

try:
    while True:
        blink_leds(pattern)
except KeyboardInterrupt:
    # Zet alle LED's uit en sluit het bord af bij afsluiten
    for pin in led_pins:
        pin.write(0)
    board.exit()