from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('/dev/ttyACM0')  # Vervang '/dev/ttyACM0' door de juiste poort

# Definieer de pins
led_pins = [board.get_pin('d:8:o'), board.get_pin('d:9:o')]
button_pin = board.get_pin('d:7:i')

def setup():
    it = util.Iterator(board)
    it.start()
    button_pin.enable_reporting()

def toggle_leds():
    """ Wissel de staat van elke LED """
    for pin in led_pins:
        pin.write(not pin.read())

# Debounce logica
last_button_state = 0
last_debounce_time = 0
debounce_delay = 0.05

try:
    setup()
    while True:
        reading = button_pin.read()
        if reading != last_button_state:
            last_debounce_time = time.time()

        if (time.time() - last_debounce_time) > debounce_delay:
            if reading != last_button_state:
                last_button_state = reading
                if reading == 1:
                    toggle_leds()

        time.sleep(0.01)  # Kleine vertraging om de loop beheersbaar te houden

except KeyboardInterrupt:
    # Zet alle LED's uit en sluit het bord af bij afsluiten
    for pin in led_pins:
        pin.write(0)
    board.exit()
