from pyfirmata import Arduino, util
import time

# Maak verbinding met het Arduino-bord
board = Arduino('/dev/ttyACM0')  # Pas dit aan naar je Arduino's COM-poort
light_sensor_pin = board.get_pin('a:0:i')  # Lichtsensor aangesloten op analoge pin A0
led_pin = board.get_pin('d:13:o')  # LED aangesloten op digitale pin 13

# Start de iterator en activeer de pin
it = util.Iterator(board)
it.start()
light_sensor_pin.enable_reporting()

# Functie om de huidige tijd in milliseconden te krijgen
current_millis = lambda: int(round(time.time() * 1000))

# Initialisatie van de timer
previous_millis = current_millis()
calibration_period = 10000  # Kalibratieperiode in milliseconden
measurements = []
calibration_done = False
threshold = None

def calculate_threshold(measurements):
    """Bereken de drempelwaarde als gemiddelde van de gemeten waarden."""
    if measurements:
        return sum(measurements) / len(measurements) * 0.8  # 80% van het gemiddelde als drempel voor 'donker'

while True:
    current_time = current_millis()
    
    # Kalibratiefase
    if not calibration_done and (current_time - previous_millis) < calibration_period:
        if (current_time - previous_millis) % 1000 == 0:  # Elke seconde een meting doen
            light_level = light_sensor_pin.read()
            if light_level is not None:
                measurements.append(light_level * 1023)  # Schaal en voeg toe aan metingen
    
    # Na kalibratie
    elif not calibration_done:
        threshold = calculate_threshold(measurements)
        calibration_done = True
        print(f"Drempelwaarde vastgesteld op: {threshold}")
        previous_millis = current_time  # Reset de timer voor normale operatie

    # Normale operatie
    else:
        if (current_time - previous_millis) >= 1000:  # Controleer elke seconde
            light_level = light_sensor_pin.read()
            if light_level is not None:
                scaled_light_level = light_level * 1023
                print(f"Actuele lichtniveau: {scaled_light_level}")
                if scaled_light_level < threshold:
                    led_pin.write(1)  # Zet LED aan
                    print("LED aan (donker gedetecteerd)")
                else:
                    led_pin.write(0)  # Zet LED uit
                    print("LED uit (licht genoeg)")
            previous_millis = current_time
