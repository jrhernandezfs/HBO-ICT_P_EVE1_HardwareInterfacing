from pyfirmata2 import Arduino
import time

# Setup the Arduino board
PORT = Arduino.AUTODETECT  # Automatically detect the correct port
board = Arduino(PORT)

print("Arduino gestart")

# Define the LED pins
redLEDPin = board.get_pin('d:13:o')  # Red LED on pin 13
greenLEDPin = board.get_pin('d:12:o')  # Green LED on pin 12
blueLEDPin = board.get_pin('d:11:o')  # Blue LED on pin 11

# Function to execute the LED sequence
def execute_sequence(sequence):
    delay_time = 0.5  # Default delay time in seconds

    for command in sequence:
        if command == 'R':
            redLEDPin.write(1)
            time.sleep(delay_time)
            redLEDPin.write(0)
        elif command == 'G':
            greenLEDPin.write(1)
            time.sleep(delay_time)
            greenLEDPin.write(0)
        elif command == 'B':
            blueLEDPin.write(1)
            time.sleep(delay_time)
            blueLEDPin.write(0)
        elif command == 'D':
            delay_time = 1  # Increase delay to 1 second
        elif command == 'F':
            delay_time = 0.25  # Decrease delay to 0.25 seconds
        else:
            print(f"Unknown command: {command}")

        time.sleep(0.1)  # Short delay between commands to avoid overlap

# Main loop to get user input and execute the sequence
print("Voer een LED-sequentie in (R voor rood, G voor groen, B voor blauw, D voor delay, F voor snel):")
while True:
    sequence = input("Enter LED sequence: ").strip().upper()
    execute_sequence(sequence)