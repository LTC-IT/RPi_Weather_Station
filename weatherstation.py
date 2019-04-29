from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

while True:
    sense.show_message("Humidity : {}%".format(round(sense.get_humidity())))
    sense.show_message("Temperature: {} celcius".format(round(sense.get_temperature())))
    sense.show_message("Pressure: {} mbar".format(round(sense.get_pressure())))
    sleep(1)