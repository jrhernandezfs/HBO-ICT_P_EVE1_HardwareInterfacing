from pyfirmata import Arduino, util
import time

# Vervang 'COM3' door de poort die je Arduino gebruikt
board = Arduino('COM9')

while True:
    board.digital[13].write(1)  # Zet de LED op pin 13 aan
    time.sleep(1)
    board.digital[13].write(0)  # Zet de LED op pin 13 uit
    time.sleep(1)