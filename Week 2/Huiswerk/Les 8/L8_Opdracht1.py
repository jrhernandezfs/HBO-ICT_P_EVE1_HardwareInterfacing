from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')
moisture_sensor = board.get_pin('a:0:i')
pump = board.get_pin('d:13:o')

it = util.Iterator(board)
it.start()
moisture_sensor.enable_reporting()

# Drempelwaarde voor lage vochtigheid
low_moisture_threshold = 0.3

def check_moisture_and_water():
    moisture_level = moisture_sensor.read()
    if moisture_level is not None:
        print(f"Huidige vochtigheid: {moisture_level}")
        if moisture_level < low_moisture_threshold:
            print("Vochtigheid is laag, start besproeiing.")
            pump.write(1)
            time.sleep(10)  # simuleer besproeiing voor 10 seconden
            pump.write(0)
            print("Besproeiing gestopt.")
        else:
            print("Vochtigheid is voldoende. Geen besproeiing nodig.")

while True:
    check_moisture_and_water()
    time.sleep(60)  # controleer elke minuut