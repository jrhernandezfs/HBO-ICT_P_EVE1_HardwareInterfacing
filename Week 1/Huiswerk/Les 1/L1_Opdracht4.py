import time
from pyfirmata import Arduino, util
import pyfirmata

# Setup de Arduino
board = Arduino('COM9')  # Vervang 'COM9' door jouw seriële poort

# Defineer pinnen
led1_pin = board.digital[13]
led2_pin = board.digital[12]
button_pin = board.digital[11]

# Variabelen voor het bijhouden van de LED- en knopstatus
led1_state = 1  # Start met de eerste LED aan
led2_state = 0  # Start met de tweede LED uit
previous_button_state = 1  # Start met de knop niet ingedrukt

# Start een iterator om de inputdata te lezen
it = util.Iterator(board)
it.start()

# Stel de knop in als INPUT met interne pull-up weerstand
button_pin.mode = pyfirmata.INPUT

# Zet de startstatus van de LED's
led1_pin.write(led1_state)
led2_pin.write(led2_state)

while True:
    # Lees de huidige staat van de knop
    button_state = button_pin.read()

    # Zorg ervoor dat de knopstatus geldig is
    if button_state is not None:
        # Check of de knopstatus is veranderd
        if button_state != previous_button_state:
            # Als de knop net is ingedrukt (overgang van HIGH naar LOW)
            if button_state == 0:
                # Wissel de LED's
                led1_state = not led1_state
                led2_state = not led2_state
                led1_pin.write(led1_state)
                led2_pin.write(led2_state)

        # Bijwerken van de vorige knopstatus
        previous_button_state = button_state

    # Een korte pauze om de loop stabiel te houden
    time.sleep(0.01)
