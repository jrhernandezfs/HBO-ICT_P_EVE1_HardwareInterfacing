from pyfirmata2 import Arduino
import time

# Connect to the Arduino
PORT = Arduino.AUTODETECT  # Automatically detect the correct port
board = Arduino(PORT)

print("Arduino gestart")
board.samplingOn(100)  # Set sampling interval to 100ms

# Callback function to handle updates from the temperature sensor
def temperature_callback(value):
    global temperature_c
    # Convert the analog value to voltage
    voltage = value * 5.0  # Convert normalized value (0-1) to voltage (0-5V)
    # Convert voltage to temperature in Celsius
    temperature_c = voltage * 100.0

# Function to control an LED based on temperature
def set_led():
    if temperature_c > 30:  # Example: Turn LED on if temperature > 30°C
        led_pin.write(1)
    else:
        led_pin.write(0)

# Configure the LM35 pin and LED pin
temp_pin = board.get_pin("a:0:i")  # Analog pin A0 for LM35 sensor
temp_pin.register_callback(temperature_callback)  # Register callback for temperature
temp_pin.enable_reporting()  # Enable reporting for the analog pin
led_pin = board.get_pin("d:9:o")  # Digital pin 9 for LED
temperature_c = 0.0  # Initialize temperature variable

# Main loop
while True:
    set_led()  # Control the LED based on the current temperature
    print(f"Current Temperature: {temperature_c:.2f} °C")
    time.sleep(1)  # Wait 1 second between updates
