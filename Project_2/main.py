from machine import Pin, I2C
from time import time,sleep
import dht, BME280, math

sensor = dht.DHT11(Pin(14))
i2c = I2C(1,scl=Pin(22), sda=Pin(21), freq=10000)
pir = Pin(18, Pin.IN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def dew_point(temperature, humidity):
    H = (math.log10(humidity)-2)/0.4343 + (17.62*temperature)/(243.12+temperature)  # dewpoint calculation from temp and hum
    Dewp = 243.12*H/(17.62-H)
    return round(Dewp, 2)

def refresh():
    bme = BME280.BME280(i2c=i2c)
    sensor.measure()
    temp = round(sensor.temperature(),2)           #temp and hum taking from dht11
    hum = round(sensor.humidity(),2)               #hum taking from dht11
    pres = bme.pressure                            #pressure taking from BME280
    dew_p = dew_point(temp,hum)
    return temp,hum,pres,dew_p

def web_page():
  html = """
<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>

<body class="bg-secondary">
    <main class="container">
        <section class="col-md-6 offset-md-3">
            <div class="border border-3 rounded-3 mt-5 bg-warning text-center">
                <h1 class="mb-5 mt-3">ESP32 Mittaukset</h1>
                <table class="table table-borderless ms-4 ms-md-5">
                    <tbody class="text-start">
                        <tr>
                            <th scope="row">Temperature</th>
                            <td><span id=temp></span> &deg;C</td>
                        </tr>
                        <tr>
                            <th scope="row">Humidity</th>
                            <td><span id=hum></span> %</td>
                        </tr>
                        <tr>
                            <th scope="row">Pressure</th>
                            <td><span id=pre></span> mbar</td>
                        </tr>
                        <tr>
                            <th scope="row">Movemont</th>
                            <td><span id=mv></span></td>
                        </tr>
                        <tr>
                            <th scope="row">Dew Point</th>
                            <td><span id=dwp></span> &deg;C</td>
                        </tr>
                    </tbody>
                </table>
                <button type="button" class="btn-danger mb-4">Update</button>
            </div>
        </section>
    </main>
    <script>
        function update_data() {
            $.get('favicon', function (data) {
                let all_data = data.split(",");
                $("#temp").text(all_data[0]);
                $("#hum").text(all_data[1]);
                $("#pre").text(all_data[2]);
                $("#dwp").text(all_data[3]);
                
            });
        }
        function update_movement() {
            $("#mv").load('mv');
        }

        $(document).ready(function () {
            update_data()
            setInterval(update_movement, 1000);
            $("button").click(function () {
                update_data()
            });
        });


    </script>
</body>

</html>
        """
  return html

def movement():
    mv =""
    if pir():
        mv = "yes"
    if not pir():
        mv = "No"
    return mv

while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        request = str(request)
        update = request.find('/favicon')
        update_mv = request.find('/mv')
        if update == 6:
            all_value = refresh()
            t = all_value[0]
            h = all_value[1]
            p = all_value[2]
            d = all_value[3]
            response = str(t) + "," + str(h) + "," + p + "," + str(d) + "," + movement()
        else:
            response = web_page()
        if update_mv == 6:
            response = movement()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        print('Failed to read sensor.')


