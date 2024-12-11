from pyfirmata2 import Arduino
import time

# Connect to the Arduino
PORT = Arduino.AUTODETECT  # Automatically detect the correct port
board = Arduino(PORT)

print("Arduino gestart")
board.samplingOn(100)  # Set sampling interval to 100ms

# Pin setup
pot_pin = board.get_pin('a:2:i')  # Potentiometer connected to analog pin A2
led_pins = [board.get_pin(f'd:{i}:o') for i in range(10, 14)]  # LED pins 10 to 13

# Global variable to store potentiometer value
pot_value = 0.0

# Callback function to handle potentiometer updates
def pot_callback(value):
    global pot_value
    pot_value = value

# Enable reporting and register callback for potentiometer
pot_pin.register_callback(pot_callback)
pot_pin.enable_reporting()

# Function to map potentiometer value to number of LEDs
def map_pot_value_to_leds(value):
    # Map potentiometer value (0-1) to number of LEDs (0-4)
    return int(value * 4)  # Scale value for 4 LEDs

# Function to control LEDs based on potentiometer value
def control_leds():
    led_count = map_pot_value_to_leds(pot_value)
    for i, led in enumerate(led_pins):
        led.write(1 if i < led_count else 0)

# Main loop
while True:
    control_leds()  # Adjust LEDs based on potentiometer value
    print(f"Potentiometer Value: {pot_value:.2f}")
    time.sleep(0.1)  # Wait 0.1 seconds between updates
