import pyfirmata2
import time

# Maak verbinding met de Arduino
PORT = pyfirmata2.Arduino.AUTODETECT  # Detecteert automatisch de juiste poort
board = pyfirmata2.Arduino(PORT)

# Definieer de LED-pins
led_11 = 11
led_12 = 12
led_13 = 13

def led_pattern():
    while True:
        # LED op pin 11 aan en uit
        board.digital[led_11].write(1)  # Zet LED aan
        time.sleep(0.5)  # Wacht 500 ms
        board.digital[led_11].write(0)  # Zet LED uit

        # LED op pin 12 aan en uit
        board.digital[led_12].write(1)  # Zet LED aan
        time.sleep(1)  # Wacht 1000 ms
        board.digital[led_12].write(0)  # Zet LED uit

        # LED op pin 13 aan en uit
        board.digital[led_13].write(1)  # Zet LED aan
        time.sleep(1.5)  # Wacht 1500 ms
        board.digital[led_13].write(0)  # Zet LED uit

# Roep de functie aan
led_pattern()