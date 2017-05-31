#!/usr/bin/python

import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 18

hum, temp = Adafruit_DHT.read_retry(sensor, pin)

read = 0
while (read == 0):
    if hum is not None and temp is not None:
        file_temp = open('/sensors/dht22/temp', 'w')
        temp = format(temp)
        file_temp.write(temp)
        file_temp.close()

        file_humidity = open('/sensors/dht22/humidity', 'w')
        humidity = format(hum)
        file_humidity.write(humidity)
        file_humidity.close()

        read = 1
    else:
        print('Failed to get reading. Try again!')
