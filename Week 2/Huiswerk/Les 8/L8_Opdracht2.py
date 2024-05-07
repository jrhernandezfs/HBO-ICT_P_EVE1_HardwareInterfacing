from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyUSB0')
light_sensor = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

it = util.Iterator(board)
it.start()
light_sensor.enable_reporting()

threshold = 0.5

while True:
    light_level = light_sensor.read()
    print(f"Sensorwaarde: {light_level}")
    if light_level is not None:
        if light_level < threshold:
            led.write(1)
            print("LED aan (lichtniveau laag)")
        else:
            led.write(0)
            print("LED uit (lichtniveau hoog)")
    else:
        print("Geen gegevens van sensor. Controleer de aansluiting.")
    time.sleep(1)