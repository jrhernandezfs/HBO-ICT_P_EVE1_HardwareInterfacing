import pyfirmata
import time

# Set up the connection to Arduino
board = pyfirmata.Arduino('COM9')  # Change 'COM3' to your Arduino port

# Define the LED pins
redLEDPin = board.get_pin('d:13:o')
yellowLEDPin = board.get_pin('d:12:o')
greenLEDPin = board.get_pin('d:11:o')

# Start an iterator thread to avoid buffer overflow
iterator = pyfirmata.util.Iterator(board)
iterator.start()

# Make sure all LEDs are off initially
redLEDPin.write(0)
greenLEDPin.write(0)
yellowLEDPin.write(0)

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
try:
    while True:
        color = input("Enter color (rood/groen/blauw): ").strip().lower()
        set_led(color)
except KeyboardInterrupt:
    # Clean up on exit
    redLEDPin.write(0)
    greenLEDPin.write(0)
    yellowLEDPin.write(0)
    board.exit()
    print("\nProgram terminated.")
