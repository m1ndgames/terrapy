#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
import subprocess
import os
from influxdb import InfluxDBClient
import datetime
import time

dbname = 'terrapy'

client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)

var = 1
while var == 1 :
    read = 0
    while (read == 0):
        try:
            now = datetime.datetime.utcnow()
            datestr = now.isoformat()
            sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)
            temp = format(sensor.read_temperature())
            temperature = float(temp)
            pressure = format(sensor.read_pressure())
            mbar = int(pressure) * 0.01

            json_body = [
                    {
                        "measurement": "bmp085",
                        "tags": {
                            "location": "anolis",
                        },
                        "time": datestr,
                        "fields": {
                            "temperature": temperature,
                            "pressure": pressure,
                            "mbar": mbar,
                        },
                    }
                ]
            client.write_points(json_body,protocol=u'json')

            read = 1
            time.sleep(5)

        except IOError:
            os.system('i2cdetect -y 1 > /dev/null')
