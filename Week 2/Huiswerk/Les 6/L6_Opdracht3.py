from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')
it = util.Iterator(board)
it.start()

# Definieer de pin voor elk verkeerslicht
green_pin = board.get_pin('d:10:o')
yellow_pin = board.get_pin('d:11:o')
red_pin = board.get_pin('d:12:o')

def operate_traffic_light(green_duration):
    green_pin.write(1)  # Groen aan
    time.sleep(green_duration)
    green_pin.write(0)  # Groen uit
    yellow_pin.write(1)  # Geel aan
    time.sleep(5)  # Geel licht duurt 5 seconden
    yellow_pin.write(0)  # Geel uit
    red_pin.write(1)  # Rood aan
    time.sleep(30)  # Rood licht duurt 30 seconden
    red_pin.write(0)  # Rood uit

while True:
    current_hour = time.localtime().tm_hour
    # Pas de duur van het groene licht aan op basis van piekuren
    if 7 <= current_hour < 9 or 16 <= current_hour < 18:  # Piekuren
        operate_traffic_light(45)
    else:
        operate_traffic_light(30)