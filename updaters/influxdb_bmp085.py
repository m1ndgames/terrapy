#!/usr/bin/python
from influxdb import InfluxDBClient
import datetime
now = datetime.datetime.utcnow()
datestr = now.isoformat()

dbname = 'testing'

file = open("/sensors/bmp085/temp", "r") 
bmp085_temp = file.read()
file = open("/sensors/bmp085/pressure", "r")
bmp085_pressure = file.read()

client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)

# Create DB
#client.create_database(dbname)

# Create Retention Policy
#client.create_retention_policy('year', '365d', 3, default=True)

json_body = [
        {
            "measurement": "bmp085",
            "tags": {
                "location": "anolis",
            },
            "time": datestr,
            "fields": {
                "temperature": bmp085_temp,
                "pressure": bmp085_pressure,
            },
        }
    ]

#print("Write points: {0}".format(json_body))
client.write_points(json_body,protocol=u'json')

#result = client.query('select temperature from dht22;')
#print("Result: {0}".format(result))
