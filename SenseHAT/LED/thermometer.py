from sense_hat import SenseHat

sense = SenseHat()

celcius = int(round(sense.get_temperature()))
fahrenheit = int(round(1.8 * celcius + 32))

sense.show_message(str(fahrenheit))
