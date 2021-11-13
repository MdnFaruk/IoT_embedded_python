from machine import Pin, I2C
from time import time,sleep
import dht, BME280
from umqtt.simple import MQTTClient

 #MQTTClient helps to connect MQTT broker
 #Create the topic string,Topics strings are used to send publications to subscribers

SERVER = "mqtt.asksensors.com"
WRITE_API_KEY = "YCt67ysZbkOKLHDhIZt9rqMG3ns7UrSp"
client = MQTTClient("umqtt_client", SERVER,"1883","faruk","farukBD33")    #port,username,password
topic = "publish/faruk/"+WRITE_API_KEY


sensor = dht.DHT11(Pin(14))
i2c = I2C(1,scl=Pin(22), sda=Pin(21), freq=10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


def read_sensor():
  try:
    bme = BME280.BME280(i2c=i2c)             #BME reading function
    sensor.measure()                         #sensor reading function
    temp = sensor.temperature()
    hum = sensor.humidity()
    pres = bme.pressure 
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = [str(temp),str(hum),pres]
      return(msg)
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

while True:
    thd = read_sensor() # receiving data as a list, calling function
    PAYLOAD = "module1="+thd[0]+"&module2="+thd[0]+"&module3="+thd[1]+"&module4="+thd[2]   # Creating a payload based on my Channel fields
    client.connect()  # connecting to the server
    client.publish(topic, PAYLOAD) # sending data to the asksensors channel
    client.disconnect()
    print(thd[0], thd[1], thd[2])  #printing to the console
    sleep(1800) # delaying sending data 30 minuts

