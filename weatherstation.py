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

# Changes the elements to true up to temp_level
for index in range (6,temp_level,-1):
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

'''
# Version 1 - Manual
# This doesn't use the list.

for row in range (temp_level, 0, -1):
    row_number = row * 8 + 4
    print(row_number)
    thermometer[row_number] = [255,0,0]

if temp_level >= 0:
    thermometer[51] = [255,0,0]
    thermometer[52] = [255,0,0]
    thermometer[53] = [255,0,0]

for row in range (temp_level, 0, -1):
    if temp_level >=2:
        row_number = row * 8 + 3
        if thermometer[row_number] == [0,0,0]:
            thermometer[row_number] = [255,0,0]

'''
# TODO: Version 2- 

sense.set_pixels(thermometer)

#while True:
    #sense.show_message("Humidity : {}%".format(round(sense.get_humidity())))
    #sense.show_message("Temperature: {} celcius".format(round(sense.get_temperature())))
    #sense.show_message("Pressure: {} mbar".format(round(sense.get_pressure())))
    #sleep(1)