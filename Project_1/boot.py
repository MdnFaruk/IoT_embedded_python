try:
  import usocket as socket
except:
  import socket

import network
from machine import Pin
from time import sleep
import dht
import math
from umqtt.simple import MQTTClient

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'faruk'
password = 'farukBD33'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "1539108"
WRITE_API_KEY = "7RAMO690B5ST093M"
client = MQTTClient("umqtt_client", SERVER)  #MQTTClient helps to connect MQTT broker
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY   #Create the topic string,Topics strings are used to send publications to subscribers

sensor = dht.DHT11(Pin(14))
