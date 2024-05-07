from pyfirmata import Arduino, util
import time

# Connect to Arduino
board = Arduino('/dev/ttyUSB0')

# Pin setup
pot_pin = board.get_pin('a:2:i')  # Potentiometer connected to analog pin A2
led_pins = [board.get_pin(f'd:{i}:o') for i in range(10, 14)]  # LED pins 10 to 13

def map_pot_value_to_leds(value):
    # This function maps the potentiometer value to the number of LEDs to light up
    return int(value * 4)  # Since we have 4 LEDs

while True:
    pot_value = pot_pin.read()
    if pot_value is not None:
        led_count = map_pot_value_to_leds(pot_value)
        for i, led in enumerate(led_pins):
            led.write(1 if i < led_count else 0)
    time.sleep(0.1)