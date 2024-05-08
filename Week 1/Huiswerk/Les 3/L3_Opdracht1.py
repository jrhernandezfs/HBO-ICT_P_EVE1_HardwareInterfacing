from pyfirmata import Arduino, util
import time

# Connect to Arduino
board = Arduino('/dev/ttyUSB0')

# Pin setup
temp_sensor = board.get_pin('a:0:i')  # Temperature sensor (TMP36) connected to analog pin A0

def read_temperature(analog_value):
    voltage = analog_value * 5.0
    temperature_c = (voltage - 0.5) * 100.0  # Convert voltage to temperature
    return temperature_c

while True:
    analog_value = temp_sensor.read()
    if analog_value is not None:
        temperature = read_temperature(analog_value)
        print(f"Current Temperature: {temperature:.2f} °C")
    time.sleep(1)
