# Dit is een voorbeeld en moet worden geïntegreerd in een testframework zoals unittest in Python.
# work in progress...

def test_led_light_level():
    expected_low_light = 0.3
    expected_high_light = 0.7
    low_light_response = simulate_light_sensor_reading(expected_low_light)
    high_light_response = simulate_light_sensor_reading(expected_high_light)
    
    assert low_light_response == 1, "LED zou aan moeten zijn bij lage lichtniveaus"
    assert high_light_response == 0, "LED zou uit moeten zijn bij hoge lichtniveaus"

def simulate_light_sensor_reading(light_level):
    threshold = 100
    if light_level < threshold:
        return 1  # LED aan
    else:
        return 0  # LED uit

test_led_light_level()
