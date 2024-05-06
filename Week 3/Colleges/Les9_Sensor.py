from pyfirmata import Arduino, util
import time

# Maak verbinding met het Arduino-bord
board = Arduino('/dev/ttyACM0')
light_sensor_pin = board.get_pin('a:0:i')  # Lichtsensor aangesloten op analoge pin A0

# Start de iterator en activeer de pin
it = util.Iterator(board)
it.start()
light_sensor_pin.enable_reporting()

# Lees de waarde van de lichtsensor
time.sleep(1)  # Wacht even voor de eerste lezing
light_level = light_sensor_pin.read()
print("Gemeten lichtniveau:", light_level)