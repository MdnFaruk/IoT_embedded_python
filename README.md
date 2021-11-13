# embedded_python

## Used dev kit
- esp32
- BME280
- DHT11
- PIR Motion Sensor

## Project_1
Make a web-based measurement application for ESP32. It must be possible to read the measured values via mobile phone or laptop using same wifi connection. 
The temperature, humidity and dew point measured values are displayed under the main page title. The user interface is formatted so that the title is centered and the measurement results are in a table with two columns and two rows.
lastly all the reading data send to to automatically to the **thingspeak** channel.

## Project_2
Make a web-based measurement application using ESP32 dev kit. It must be possible to read 
the measured values via mobile phone or wifi connection.
The customer's display shows the measured values of pressure, DHT_temp, humidity and 
dewpoint. The appearance is shaped so that the title is centered and the measurement results are in a 
table with two columns and four rows. In addition to the above, the table 
also shows whether the ESP32's PIR sensor has responded to movement. The customer's 
display shows YES or NO on the fifth line of the table. The view would be as follows when 
the PIR sensor has responded to the movement. Adding a UPDATE button to 
the window that appears to the customer, which, when clicked, refreshes the screen and does 
not need to be loaded from the address bar.

## Project_3
Create one sensor for the cloud service and 4 modules for it. Define the modules so that 
module1 contains the temperature measured values in table form, module2 is the 
temperature as a line graph, module3 is the relative humidity as a line graph, and module4 is 
the pressure line graph. Define a measurement interval of 30 minutes in your code. 
 
Tasks required for grade 3:  
 
In addition to the above, create a new sensor (Sensor2) and four modules. Add measurement 
data to these first three modules so that the measured Dallas_Temperatute information is 
displayed as a Line-type graph and the PIR sensor ON / OFF information is displayed in 
Binary-type as well as table format. Add the necessary codes to ESP32 for luminosity and 
PIR sensor measurements. Also specify in your code the measurement interval for these 
sensors to be 30min. 
 
Tasks required for grade 4:  
 
The operation of a PIR sensor does not make sense if only every 30 minutes it is checked 
whether there is movement in the area of the sensor, so changes are made to the code (use 
interrupts in your code). 
The identification information of the PIR sensor is to be displayed immediately in the graph, 
ie when the sensor detects movement, the information is immediately sent to the cloud and it 
is displayed in the Binary graph (ON) as well as in the table. When the movement is not 
detected for a moment, so is the information in the cloud (NO). 
 
Tasks required for grade 5:  
 
JSON is an open standardized data presentation and communication format that uses human 
readable text to store and send objects consisting of name / value pairs. 
Your task with ESP32 is to retrieve temperature information from Kajaani (or another city to 
be found) from the weather service and take that information to Asksensors' cloud service 
Sensor2's module4. 
 
Temperature information (and all other weather information) is retrieved from the 
OpenWeather service (https://openweathermap.org/) in JSON type.
