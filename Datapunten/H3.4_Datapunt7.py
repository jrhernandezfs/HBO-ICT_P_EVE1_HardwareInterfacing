from pyfirmata import Arduino, util
import time

# Setup
board = Arduino('/dev/ttyUSB0')  # Pas de poort aan naar je Arduino poort
it = util.Iterator(board)
it.start()

# Pin configuratie voor sensoren en LEDs
sensor_a = board.get_pin('d:2:i')  # Sensor A op pin 2 voor binnenkomst
sensor_b = board.get_pin('d:3:i')  # Sensor B op pin 3 voor vertrek
red_led = board.get_pin('d:10:o')
yellow_led = board.get_pin('d:9:o')
green_led = board.get_pin('d:8:o')

# Attracties definieren
attracties = [
    {"naam": "Achtbaan", "capaciteit": 100, "wachtrij": 0},
    {"naam": "Draaimolen", "capaciteit": 50, "wachtrij": 0},
    {"naam": "Waterglijbaan", "capaciteit": 80, "wachtrij": 0}
]

def kies_attractie():
    for idx, attractie in enumerate(attracties):
        print(f"{idx + 1}. {attractie['naam']}")
    keuze = int(input("Kies een attractie: ")) - 1
    return attracties[keuze]

def update_traffic_light(attractie):
    if attractie["wachtrij"] == 0:
        green_led.write(0)
        yellow_led.write(0)
        red_led.write(1)
    elif attractie["wachtrij"] < attractie["capaciteit"]:
        green_led.write(1)
        yellow_led.write(0)
        red_led.write(0)
    else:
        green_led.write(0)
        yellow_led.write(1)
        red_led.write(0)

def check_sensors(attractie):
    enter = sensor_a.read()
    exit = sensor_b.read()
    
    if enter:
        if attractie["wachtrij"] < attractie["capaciteit"]:
            attractie["wachtrij"] += 1
        else:
            print("Maximale capaciteit bereikt!")
    if exit:
        if attractie["wachtrij"] > 0:
            attractie["wachtrij"] -= 1
        else:
            print("Wachtrij is al leeg!")
    update_traffic_light(attractie)

# Attractie kiezen
gekozen_attractie = kies_attractie()

# Polling lus
while True:
    check_sensors(gekozen_attractie)
    print(f"Huidige wachtrijlengte voor {gekozen_attractie['naam']}: {gekozen_attractie['wachtrij']}")
    time.sleep(0.5)  # Halve seconde wachten voor stabiliteit
