from pyfirmata2 import Arduino
import time

# Connect to the Arduino
PORT = Arduino.AUTODETECT  # Automatically detect the correct port
board = Arduino(PORT)

print("Arduino gestart")
board.samplingOn(100)  # Set sampling interval to 100ms

# Pin setup
ldr_sensor = board.get_pin('a:1:i')  # LDR connected to analog pin A1
led_pin = board.get_pin('d:13:o')   # LED connected to pin 13

# Global variable to store the current light intensity
light_intensity = 0.0

# Callback function to handle LDR updates
def ldr_callback(value):
    global light_intensity
    light_intensity = value

# Enable reporting and register callback for LDR
ldr_sensor.register_callback(ldr_callback)
ldr_sensor.enable_reporting()

# Function to check light intensity and control the LED
def control_led():
    # Adjust the threshold as needed based on your lighting conditions
    if light_intensity < 0.1:  # It's dark
        led_pin.write(1)  # Turn on LED
    else:
        led_pin.write(0)  # Turn off LED

# Main loop
while True:
    control_led()  # Adjust LED based on current light intensity
    print(f"Light Intensity: {light_intensity:.2f}")
    time.sleep(0.5)  # Wait 0.5 seconds between updates
