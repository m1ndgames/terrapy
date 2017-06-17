#!/usr/bin/python
from influxdb import InfluxDBClient
import datetime
now = datetime.datetime.utcnow()
datestr = now.isoformat()

dbname = 'testing'

file = open("/sensors/dht22/temp", "r") 
dht22_temp = file.read()
file = open("/sensors/dht22/humidity", "r")
dht22_humidity = file.read()

client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)

# Create DB
#client.create_database(dbname)

# Create Retention Policy
#client.create_retention_policy('year', '365d', 3, default=True)

json_body = [
        {
            "measurement": "dht22",
            "tags": {
                "location": "anolis",
            },
            "time": datestr,
            "fields": {
                "temperature": dht22_temp,
                "humidity": dht22_humidity,
            },
        }
    ]

#print("Write points: {0}".format(json_body))
client.write_points(json_body,protocol=u'json')

#result = client.query('select temperature from dht22;')
#print("Result: {0}".format(result))
