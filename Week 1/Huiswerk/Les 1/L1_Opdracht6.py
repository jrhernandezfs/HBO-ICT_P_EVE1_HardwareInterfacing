import pyfirmata
import time

# Setup the Arduino board
board = pyfirmata.Arduino('COM9')  # Change 'COM3' to your Arduino port

# Define the LED pins
redLEDPin = board.get_pin('d:13:o')
greenLEDPin = board.get_pin('d:12:o')
blueLEDPin = board.get_pin('d:11:o')

# Start an iterator thread to avoid buffer overflow
iterator = pyfirmata.util.Iterator(board)
iterator.start()

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

try:
    while True:
        sequence = input("Enter LED sequence (R for red, G for green, B for blue, D for delay, F for fast): ").strip().upper()
        execute_sequence(sequence)
except KeyboardInterrupt:
    print("\nProgram terminated.")
finally:
    redLEDPin.write(0)
    greenLEDPin.write(0)
    blueLEDPin.write(0)
    board.exit()
