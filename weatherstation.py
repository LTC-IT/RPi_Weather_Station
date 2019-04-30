from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

b = [0,0,0]
w = [255,255,255]
r = [255,0,0]

max = 40
min = 0

temp_range = [False, False, False, False, False, False, False]

temp_level = round(sense.get_temperature() / 7)

print (temp_level)

for index in range (0,temp_level+1):
    temp_range[index] = True
    
print(temp_range)

thermometer = [
    b,b,w,b,b,w,b,b,
    b,b,w,w,b,w,b,b,
    b,b,w,b,b,w,b,b,
    b,b,w,w,b,w,b,b,
    b,b,w,b,b,w,b,b,
    b,b,w,w,b,w,w,b,
    b,b,w,b,b,b,w,b,
    b,b,w,w,w,w,w,b
    ]

sense.set_pixels(thermometer)

#while True:
    #sense.show_message("Humidity : {}%".format(round(sense.get_humidity())))
    #sense.show_message("Temperature: {} celcius".format(round(sense.get_temperature())))
    #sense.show_message("Pressure: {} mbar".format(round(sense.get_pressure())))
    #sleep(1)