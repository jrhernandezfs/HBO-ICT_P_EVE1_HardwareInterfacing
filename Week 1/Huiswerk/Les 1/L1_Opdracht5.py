from pyfirmata2 import Arduino

# Set up the connection to Arduino
PORT = Arduino.AUTODETECT  # Automatically detect the correct port
board = Arduino(PORT)

print("Arduino gestart")

# Define the LED pins
redLEDPin = board.get_pin('d:13:o')  # Pin for red LED
yellowLEDPin = board.get_pin('d:12:o')  # Pin for yellow LED
greenLEDPin = board.get_pin('d:11:o')  # Pin for green LED

# Make sure all LEDs are off initially
redLEDPin.write(0)
greenLEDPin.write(0)
yellowLEDPin.write(0)

# Function to set LED color
def set_led(color):
    if color == 'rood':
        redLEDPin.write(1)
        greenLEDPin.write(0)
        yellowLEDPin.write(0)
    elif color == 'geel':
        redLEDPin.write(0)
        greenLEDPin.write(0)
        yellowLEDPin.write(1)
    elif color == 'groen':
        redLEDPin.write(0)
        greenLEDPin.write(1)
        yellowLEDPin.write(0)
    else:
        # Turn off all LEDs if the input does not match any color
        redLEDPin.write(0)
        greenLEDPin.write(0)
        yellowLEDPin.write(0)

# Main loop to take user input
print("Voer een kleur in (rood/groen/geel), of druk op Ctrl+C om te stoppen.")
while True:
    color = input("Enter color (rood/groen/geel): ").strip().lower()
    set_led(color)