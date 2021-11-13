import json,time
from umqtt.simple import MQTTClient
import urequests as requests

SERVER = "mqtt.asksensors.com"
WRITE_API_KEY = "yCrheQNro8ucUO6uW7eUN5JY3lhahepP"
client = MQTTClient("umqtt_client", SERVER,"1883","faruk","farukBD33")
topic = "publish/faruk/"+WRITE_API_KEY

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=pori&appid=b0adb4b658cf1f94ab97f31275df16bd")  # getting weather information from this API
    json_data = response.json()           #converting into json
    temp = json_data["main"] ["temp"]     #taking only temperature
    temp = round(temp - 273.15, 2)        #converting kelvin to degree celcius
    PAYLOAD = "module4="+ str(temp)
    client.connect()  # connecting to the server
    client.publish(topic, PAYLOAD) # sending data to the asksensors channel
    client.disconnect()
    
    print(temp) 
    time.sleep(5)      #delaying 5 seconds for checking purpose


