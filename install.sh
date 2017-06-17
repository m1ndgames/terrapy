#!/bin/sh

sudo mkdir -p /sensors/bmp085
sudo mkdir -p /sensors/dht22

sudo apt-get upgrade
sudo apt-get install build-essential python-dev git i2c-tools

# Adafruit python GPIO lib
git clone https://github.com/adafruit/Adafruit_Python_GPIO
cd Adafruit_Python_GPIO
sudo python setup.py install
cd ..

# Adafruit python DHT lib
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
cd ..

# Adafruit python BMP lib
git clone https://github.com/adafruit/Adafruit_Python_BMP
cd Adafruit_Python_BMP
sudo python setup.py install
cd ..

# Create influxdb Database and Retention
./install/influxdb.py
