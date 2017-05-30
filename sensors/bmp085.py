#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
import subprocess
import os

read = 0
while (read == 0):
    try:
        sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

        file_temp = open('/sensors/bmp085/temp', 'w')
        temp = format(sensor.read_temperature())
        file_temp.write(temp)
        file_temp.close()

        file_pressure = open('/sensors/bmp085/pressure', 'w')
        pressure = format(sensor.read_pressure())
        file_pressure.write(pressure)
        file_pressure.close()

        file_altitude = open('/sensors/bmp085/altitude', 'w')
        altitude = format(sensor.read_altitude())
        file_altitude.write(altitude)
        file_altitude.close()

        file_sealevelpressure = open('/sensors/bmp085/altitude', 'w')
        sealevelpressure = format(sensor.read_altitude())
        file_sealevelpressure.write(sealevelpressure)
        file_sealevelpressure.close()

        read = 1

    except IOError:
        os.system('i2cdetect -y 1 > /dev/null')
