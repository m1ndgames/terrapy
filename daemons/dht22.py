#!/usr/bin/python
import subprocess
import os
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 18
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
            hum, temp = Adafruit_DHT.read_retry(sensor, pin)

            json_body = [
                    {
                        "measurement": "dht22",
                        "tags": {
                            "location": "anolis",
                        },
                        "time": datestr,
                        "fields": {
                            "humidity": hum,
                            "temperature": temp,
                        },
                    }
                ]
            client.write_points(json_body,protocol=u'json')

            read = 1
            time.sleep(5)

        except IOError:
            os.system('i2cdetect -y 1 > /dev/null')
