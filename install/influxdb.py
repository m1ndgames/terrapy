#!/usr/bin/python
from influxdb import InfluxDBClient

dbname = 'terrapy'

client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)

# Create DB
client.create_database(dbname)

# Create Retention Policy
client.create_retention_policy('year', '365d', 3, default=True)
