from pyfirmata import Arduino, util
import time

# Verbind met de Arduino
board = Arduino('/dev/ttyACM0')

# Configureer de pins
sensor_pin = board.get_pin('a:0:i')  # Lichtsensor op pin A0
led_pin = board.get_pin('d:13:o')    # LED op pin 13

# Start de iterator thread om input van de analoge pin te lezen
it = util.Iterator(board)
it.start()
sensor_pin.enable_reporting()

# Drempelwaarde voor lichtintensiteit
threshold = 0.5

while True:
    light_level = sensor_pin.read()  # Lees de lichtsensor
    print("Sensorwaarde:", light_level)  # Print de gelezen waarde van de sensor
    if light_level is None:
        print("Geen gegevens van sensor. Controleer de aansluiting.")
    elif light_level < threshold:
        led_pin.write(1)  # Zet LED aan
        print("LED aan (lichtniveau laag)")
    else:
        led_pin.write(0)  # Zet LED uit
        print("LED uit (lichtniveau hoog)")
    time.sleep(1)  # Wacht voor 1 seconde