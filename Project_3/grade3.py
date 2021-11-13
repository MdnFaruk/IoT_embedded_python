from machine import Pin
from time import time,sleep
import machine, onewire, ds18x20
from umqtt.simple import MQTTClient

SERVER = "mqtt.asksensors.com"
WRITE_API_KEY = "yCrheQNro8ucUO6uW7eUN5JY3lhahepP"
client = MQTTClient("umqtt_client", SERVER,"1883","faruk","farukBD33")
topic = "publish/faruk/"+WRITE_API_KEY

pir = Pin(18, Pin.IN)
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


def movement():                              #pir sensor checking movement
    mv =""
    if pir():
        mv = 1
    if not pir():
        mv = 0
    return mv

def temp_dallas():                             #temperature taking function from dallas 18B20
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        if isinstance(temp, float):
          msg = round(temp, 2)
          return str(msg)

while True:

    PAYLOAD = "module1="+temp_dallas()+"&module2=%d"% movement()+"&module3="+str(movement())   # Creating a payload based on my Channel fields
    client.connect()  # connecting to the server
    client.publish(topic, PAYLOAD) # sending data to the thingspeak channel
    client.disconnect()
    print(temp_dallas())
    print(movement())  
    sleep(1800) # delaying sending data 30 minuts


