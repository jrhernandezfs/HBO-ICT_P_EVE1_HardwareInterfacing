from pyfirmata import Arduino, util
import time

# Connect to Arduino
board = Arduino('/dev/ttyUSB0')

# Pin setup
pir_sensor = board.get_pin('d:7:i')  # PIR sensor connected to pin 7
alarm = board.get_pin('d:13:o')      # LED or buzzer connected to pin 13

while True:
    if pir_sensor.read() == True:
        alarm.write(1)  # Activate alarm
        print("Beweging gedetecteerd!")
        time.sleep(5)   # Alarm blijft 5 seconden aan
        alarm.write(0)  # Deactivate alarm
    time.sleep(0.5)