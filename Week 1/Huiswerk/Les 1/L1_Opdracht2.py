import time
from pyfirmata import Arduino, util

# Stel het board in
board = Arduino('COM3')  # Vervang 'COM3' met de poort die jouw Arduino gebruikt

# Zorg ervoor dat de LED pins als output zijn ingesteld
led_11 = board.get_pin('d:11:o')
led_12 = board.get_pin('d:12:o')
led_13 = board.get_pin('d:13:o')

def led_pattern():
    while True:
        # LED op pin 11 aan en uit
        led_11.write(1)  # Zet LED aan
        time.sleep(0.5)  # Wacht 500 ms
        led_11.write(0)  # Zet LED uit
        
        # LED op pin 12 aan en uit
        led_12.write(1)  # Zet LED aan
        time.sleep(1)    # Wacht 1000 ms
        led_12.write(0)  # Zet LED uit
        
        # LED op pin 13 aan en uit
        led_13.write(1)  # Zet LED aan
        time.sleep(1.5)  # Wacht 1500 ms
        led_13.write(0)  # Zet LED uit

try:
    led_pattern()
except KeyboardInterrupt:
    print("Programma gestopt.")
    board.exit()
