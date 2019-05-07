from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

b = [0,0,0]
w = [255,255,255]
r = [255,0,0]

def temperature_display():
    #TODO Scale the values to range between min and max.

    max = 40
    min = 0

    temp_range = [False, False, False, False, False, False, False]



    temp_level = round(sense.get_temperature() / 7)

    print (temp_level)

    # Changes the elements to true up to temp_level
    #for index in range (6,temp_level,-1):
    for counter in range (0,temp_level):
        temp_range[6-counter] = True
        
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

    if temp_range[0] == True:
        thermometer[3] = [255,0,0]
        thermometer[4] = [255,0,0]

    if temp_range[1] == True:
        thermometer[12] = [255,0,0]
        
    if temp_range[2] == True:
        thermometer[19] = [255,0,0]
        thermometer[20] = [255,0,0]

    if temp_range[3] == True:
        thermometer[28] = [255,0,0]

    if temp_range[4] == True:
        thermometer[35] = [255,0,0]
        thermometer[36] = [255,0,0]

    if temp_range[5] == True:
        thermometer[44] = [255,0,0]

    if temp_range[6] == True:
        thermometer[51] = [255,0,0]
        thermometer[52] = [255,0,0]
        thermometer[53] = [255,0,0]

    sense.set_pixels(thermometer)


def humidity_display():
    humidity = round(sense.get_humidity())
    
    b = [0,0,0]
    w = [0,0,0]
    
    humidity_gradient = round(humidity / 10)
    
    print (humidity_gradient)
    
    # l for level
    l = humidity_gradient * 25
    
    w = [l,l,l]
    
    cloud = [
        b,b,b,b,b,b,b,b,
        b,b,b,w,w,w,b,b,
        b,w,w,w,w,w,w,b,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,b,
        b,b,w,w,w,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    sense.set_pixels(cloud)

def barometer_display():
    bar = round(sense.get_pressure())
    
    b = [0,0,0]
    
    sunny = [
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0,
        b,b,b,b,b,0,0,0
        ]
    
    r = [255,0,0]
    
    up = [
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,r,r,r,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b
        ]
    down = [
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,b,r,b,
        0,0,0,0,0,r,r,r,
        0,0,0,0,0,b,r,b
        ]
    stable = [
        0,0,0,0,0,b,b,b,
        0,0,0,0,0,b,b,b,
        0,0,0,0,0,b,b,b,
        0,0,0,0,0,r,r,r,
        0,0,0,0,0,r,r,r,
        0,0,0,0,0,b,b,b,
        0,0,0,0,0,b,b,b,
        0,0,0,0,0,b,b,b
        ]
    
    

while True:
    #temperature_display()
    #humidity_display()
    barometer_display()
    #sense.show_message("Humidity : {}%".format(round(sense.get_humidity())))
    #sense.show_message("Temperature: {} celcius".format(round(sense.get_temperature())))
    #sense.show_message("Pressure: {} mbar".format(round(sense.get_pressure())))
    sleep(0.5)
