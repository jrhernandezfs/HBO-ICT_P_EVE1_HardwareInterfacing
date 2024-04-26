from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('COM3')  # Vervang 'COM3' door de juiste COM-poort

# Definieer de LED pins
led_pins = {
    'rood': board.get_pin('d:9:o'),
    'groen': board.get_pin('d:10:o'),
    'blauw': board.get_pin('d:11:o')
}

def control_led(color, state):
    """ Schakel een specifieke LED aan of uit """
    if color in led_pins:
        led_pins[color].write(state)

try:
    while True:
        color_input = input("Voer een kleur in ('rood', 'groen', 'blauw' of 'stop' om te stoppen): ").lower()
        if color_input == 'stop':
            break
        # Schakel de geselecteerde LED in of uit
        control_led(color_input, 1)  # Zet LED aan
        time.sleep(1)  # Laat het 1 seconde aan
        control_led(color_input, 0)  # Zet LED uit
finally:
    # Zet alle LED's uit en sluit het bord af bij afsluiten
    for color in led_pins:
        led_pins[color].write(0)
    board.exit()