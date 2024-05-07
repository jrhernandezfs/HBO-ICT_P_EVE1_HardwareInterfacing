from pyfirmata import Arduino, util, SERVO
import time

board = Arduino('/dev/ttyUSB0')
ultrasonic_pin = board.get_pin('d:7:i')
servo_pin = board.get_pin('d:9:o')

board.digital[9].mode = SERVO

def set_servo_angle(angle):
    board.digital[9].write(angle)

vehicle_count = 0
max_capacity = 50

while True:
    if ultrasonic_pin.read() == 1:  # Detecteer voertuig
        if vehicle_count < max_capacity:
            vehicle_count += 1
            set_servo_angle(90)  # Open slagboom
            time.sleep(5)
            set_servo_angle(0)   # Sluit slagboom
        else:
            print("Garage vol")
    time.sleep(1)