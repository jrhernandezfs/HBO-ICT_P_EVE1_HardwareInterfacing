from pyfirmata import Arduino, util
import time

# Connect to Arduino
board = Arduino('/dev/ttyUSB0')

# Pin setup
ldr_sensor = board.get_pin('a:1:i')  # LDR connected to analog pin A1
led_pin = board.get_pin('d:13:o')    # LED connected to pin 13

def check_light_intensity(analog_value):
    # You may need to adjust the threshold based on your lighting conditions
    return analog_value < 0.1  # Returns True if it's dark

while True:
    light_intensity = ldr_sensor.read()
    if light_intensity is not None:
        if check_light_intensity(light_intensity):
            led_pin.write(1)  # Turn on LED
        else:
            led_pin.write(0)  # Turn off LED
    time.sleep(0.5)