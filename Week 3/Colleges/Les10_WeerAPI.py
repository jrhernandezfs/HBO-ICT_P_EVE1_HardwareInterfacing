from pyfirmata import Arduino, util
import requests
import time

# Maak verbinding met het Arduino-bord
board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
it.start()

# Definieer de pins voor de RGB LED
red_pin = board.get_pin('d:11:p')  # PWM pin voor rood
green_pin = board.get_pin('d:10:p')  # PWM pin voor groen
blue_pin = board.get_pin('d:9:p')  # PWM pin voor blauw

def get_temperature():
    # Vervang 'your_api_key' met je werkelijke KNMI API sleutel
    response = requests.get("http://api.knmi.nl/weatherdata/temperature?apikey=your_api_key")
    data = response.json()
    return data['temperature']

def update_led(temperature):
    if temperature < 10:
        red_pin.write(0)
        green_pin.write(1)
        blue_pin.write(0)
    elif 10 <= temperature <= 20:
        red_pin.write(0)
        green_pin.write(0.5)
        blue_pin.write(0)
    elif temperature > 30:
        red_pin.write(1)
        green_pin.write(0)
        blue_pin.write(0)

while True:
    temperature = get_temperature()
    update_led(temperature)
    time.sleep(600)  # Update elke 10 minuten
