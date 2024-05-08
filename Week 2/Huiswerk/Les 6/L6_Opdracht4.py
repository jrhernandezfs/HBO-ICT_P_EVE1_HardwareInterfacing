from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')
temp_sensor = board.get_pin('a:0:i')
fan_pin = board.get_pin('d:3:p')

it = util.Iterator(board)
it.start()
temp_sensor.enable_reporting()

# Defineer thresholds en ventilatorsnelheden
LOW_TEMP_THRESHOLD = 20
HIGH_TEMP_THRESHOLD = 30
FAN_SPEED_LOW = 0.3
FAN_SPEED_HIGH = 1.0

state = 'LOW'  # Begin staat

while True:
    temperature = temp_sensor.read()
    if temperature is not None:
        if state == 'LOW' and temperature > HIGH_TEMP_THRESHOLD:
            state = 'HIGH'
            fan_pin.write(FAN_SPEED_HIGH)
        elif state == 'HIGH' and temperature < LOW_TEMP_THRESHOLD:
            state = 'LOW'
            fan_pin.write(FAN_SPEED_LOW)
    time.sleep(1)