from pyfirmata import Arduino, util
import time

# Setup
board = Arduino('/dev/ttyUSB0')  # Pas de poort aan naar je Arduino poort
it = util.Iterator(board)
it.start()

# Pin configuratie
sensor_a = board.get_pin('d:2:i')  # Sensor A op pin 2
sensor_b = board.get_pin('d:3:i')  # Sensor B op pin 3
red_led = board.get_pin('d:10:o')
yellow_led = board.get_pin('d:9:o')
green_led = board.get_pin('d:8:o')

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

def check_sensors():
    global queue_length
    enter = sensor_a.read()
    exit = sensor_b.read()
    
    if enter:
        if queue_length < max_capacity:
            queue_length += 1
        else:
            print("Maximale capaciteit bereikt!")
    if exit:
        if queue_length > 0:
            queue_length -= 1
        else:
            print("Wachtrij is al leeg!")
    update_traffic_light()

# Polling lus
while True:
    check_sensors()
    print(f"Huidige wachtrijlengte: {queue_length}")
    time.sleep(0.5)  # Halve seconde wachten voor stabiliteit