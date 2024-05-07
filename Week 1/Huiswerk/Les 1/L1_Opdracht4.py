from pyfirmata import Arduino, util
import time

# Maak verbinding met de Arduino
board = Arduino('COM3')  # Vervang 'COM3' door de juiste COM-poort

# Stel een iterator in om te luisteren naar inkomende data
it = util.Iterator(board)
it.start()

# Definieer de STRING_DATA commando voor het verzenden van strings
STRING_DATA = 0x71

# Stel een variabele in voor het verzenden van data
input_pin = board.get_pin('d:7:i')  # Stel pin 7 in als invoer (voor een drukknop bijvoorbeeld)
input_pin.enable_reporting()

def send_and_echo(input_string):
    """ Verzend een string naar de Arduino en print wat terugkomt. """
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(input_string))
    time.sleep(0.1)  # Wacht even op de Arduino om te reageren
    while board.bytes_available():
        data = board.receive_sysex()
        echo = util.two_byte_iter_to_str(data)
        print("Echo van Arduino:", echo)

try:
    while True:
        user_input = input("Voer een string in (type 'exit' om te stoppen): ")
        if user_input.lower() == 'exit':
            break
        send_and_echo(user_input)
finally:
    board.exit()  # Sluit de verbinding netjes af