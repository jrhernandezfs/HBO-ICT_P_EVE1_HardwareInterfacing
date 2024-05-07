from pyfirmata import Arduino, util
import time

# Connect to Arduino
board = Arduino('/dev/ttyUSB0')

# Pin setup
temp_sensor = board.get_pin('a:0:i')  # TMP36 connected to analog pin A0
fan_pin = board.get_pin('d:3:p')      # Fan connected through a motor driver to pin 3

def read_temperature(analog_value):
    voltage = analog_value * 5.0
    temperature_c = (voltage - 0.5) * 100.0  # Convert voltage to temperature
    return temperature_c

while True:
    temperature = read_temperature(temp_sensor.read())
    if temperature < 25:
        fan_speed = 0
    elif temperature < 30:
        fan_speed = 0.5
    else:
        fan_speed = 1

    fan_pin.write(fan_speed)  # Set fan speed
    print(f"Huidige temperatuur: {temperature:.2f} °C, Fan snelheid: {fan_speed:.2f}")
    time.sleep(1)