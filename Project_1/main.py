def dew_point(temperature, humidity):
    H = (math.log10(humidity)-2)/0.4343 + (17.62*temperature)/(243.12+temperature)  # dewpoint calculation from temp and hum
    Dewp = 243.12*H/(17.62-H)
    return round(Dewp, 2)

def read_sensor():
  try:
    sensor.measure()                         #sensor reding function
    temp = sensor.temperature()
    hum = sensor.humidity()
    Dp = dew_point(temp,hum)
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = [str(temp),str(hum),str(Dp)]
      return(msg)
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')


while True:
    thd = read_sensor() # receiving data as a list, calling function
    payload = "field1="+thd[0]+"&field2="+thd[1]+"&field3="+thd[2]   # Creating a payload based on my Channel fields
    print(thd[0], thd[1], thd[2])  #printing to the console
    client.connect()  # connecting to the server
    client.publish(topic, payload) # sending data to the thingspeak channel
    client.disconnect()
    sleep(30) # delaying sending data 30 seconds
    
