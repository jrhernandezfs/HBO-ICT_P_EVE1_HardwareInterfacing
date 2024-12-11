from pyfirmata2 import Arduino
import time

# Setup de Arduino
PORT = Arduino.AUTODETECT  # Detecteert automatisch de juiste poort
board = Arduino(PORT)

print("Arduino gestart")
board.samplingOn(100)  # Stel de bemonsteringsinterval in op 100 ms

# Variabelen voor het bijhouden van de LED- en knopstatus
led1_state = 1  # Start met de eerste LED aan
led2_state = 0  # Start met de tweede LED uit
previous_button_state = 1  # Start met de knop niet ingedrukt

# Callback-functie voor de knop
def button_callback(value):
    global led1_state, led2_state, previous_button_state

    # Controleer of de knopstatus geldig is en gewijzigd
    if value is not None and value != previous_button_state:
        # Als de knop net is ingedrukt (overgang van HIGH naar LOW)
        if value == 0:
            # Wissel de LED-staten
            led1_state = not led1_state
            led2_state = not led2_state
            led1_pin.write(led1_state)
            led2_pin.write(led2_state)

        # Bijwerken van de vorige knopstatus
        previous_button_state = value

# Defineer pinnen
led1_pin = board.get_pin("d:13:o")  # Digitale pin 13 als output
led2_pin = board.get_pin("d:12:o")  # Digitale pin 12 als output
button_pin = board.get_pin("d:2:i")  # Digitale pin 11 als input

# Stel de callback in voor de knop
button_pin.register_callback(button_callback)
button_pin.enable_reporting()

# Zet de startstatus van de LED's
led1_pin.write(led1_state)
led2_pin.write(led2_state)

# Hoofdloop
while True:
    # De callback verzorgt alle logica, dus we hoeven hier niets te doen
    time.sleep(0.01)  # Korte pauze voor stabiliteit