from pyfirmata import Arduino, util
import time

# Setup
board = Arduino('/dev/ttyUSB0')  # Pas de poort aan naar je Arduino poort
it = util.Iterator(board)
it.start()

# Pin configuratie
red_led = board.get_pin('d:10:o')  # Rode LED op pin 10
yellow_led = board.get_pin('d:9:o')  # Gele LED op pin 9
green_led = board.get_pin('d:8:o')  # Groene LED op pin 8

queue_length = 0
max_capacity = 50  # Maximale capaciteit van de wachtrij

def update_traffic_light():
    if queue_length == 0:
        green_led.write(0)
        yellow_led.write(0)
        red_led.write(1)
    elif queue_length < max_capacity:
        green_led.write(1)
        yellow_led.write(0)
        red_led.write(0)
    else:
        green_led.write(0)
        yellow_led.write(1)
        red_led.write(0)

def process_input(command):
    global queue_length
    action, number = command[0], int(command[1:])
    
    if action == 'I':  # Personen betreden de wachtrij
        if queue_length + number > max_capacity:
            print("Capaciteit bereikt! Kan niet meer toevoegen.")
        else:
            queue_length += number
    elif action == 'O':  # Personen verlaten de wachtrij
        if queue_length - number < 0:
            print("Wachtrij kan niet negatief zijn!")
        else:
            queue_length -= number
    update_traffic_light()

# Simulatie van input verwerking
while True:
    input_command = input("Voer commando in ('I' + aantal of 'O' + aantal): ")
    process_input(input_command)
    print(f"Huidige wachtrijlengte: {queue_length}")
    time.sleep(1)
